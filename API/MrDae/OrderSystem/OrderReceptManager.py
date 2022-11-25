from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from MrDae import processing

from .OrderEntity import OrderEntity as OE
from .OrderEntity import OrderDetailEntity as ODE

from ..CustomerArtifacts.CustomerAccountEntity import CustomerAccountEntity as CAE
from ..CustomerArtifacts.CustomerManager import CustomerRankManager as CRM

class OrderList(APIView):
    def get(self, request):
        try: 
            customer_id = processing.getUserID(request.COOKIES)
            return Response(OE.getlist(customer_id))
        except:
            return Response("No Authorized", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request): # 고객에 대해서 주문 완성!
        try:
            customer_id = processing.getUserID(request.COOKIES)
            user_info = CAE.get(customer_id)
            order_info = processing.getUserInfo(request.data.get('order_info'), user_info) # 배달 정보 가져오기
            price = request.data.get("price", 0)
            detail = request.data.get("order_detail")
            try:
                order_id, customer_order_id = OE.add(customer_id, order_info, int(price))
                try:
                    response = ODE.add(order_id, detail) # 주문

                    print("{}번째 고객의 {}번째 주문 성공".format(customer_id, customer_order_id))
                    CRM.updateRank(customer_id, user_info['rank'])
                    return Response(response , status=status.HTTP_201_CREATED)
                except:
                    OE.delete(order_id)
                    return (Response("Order Detail Error", status=status.HTTP_400_BAD_REQUEST))
            except:
                return Response("Order Error", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Login Error", status=status.HTTP_401_UNAUTHORIZED)

class OrderDetail(APIView): # 고객용 주문 상세를 요청
    def get(self, request, customer_orderid):
        try:
            try:
                customer_id = processing.getUserID(request.COOKIES)
                return Response(OE.get(customer_id, customer_orderid))
            except:
                return Response("{}번째 계정의 {}번째 주문은 존재하지 않습니다.".format(customer_id, customer_id), status=status.HTTP_404_NOT_FOUND)
        except:
            return Response("Login Error", status=status.HTTP_401_UNAUTHORIZED)

class OrderReceptManager:
    def makeOrder():
        return OrderList
    def getOrderList():
        return OrderList
    def getOrderDetail():
        return OrderDetail
        