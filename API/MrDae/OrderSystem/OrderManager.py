from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .OrderEntity import OrderEntity as OE
from .OrderEntity import OrderDetailEntity as ODE

class OrderList(APIView):
    def get(self, request):
        return Response(OE.getlist())

class OrderDetail(APIView):
    def get(self, request, orderid):
        try:
            return Response(OE.getDetail(orderid))
        except:
            return Response("{}번째 주문은 존재하지 않습니다.".format(orderid), status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, orderid):
        state, response = OE.changeState(orderid)
        if state:
            return Response(response)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CookOrder(APIView):
    def get(self, request):
        return Response(OE.filter(4))
class DeliveryOrder(APIView):
    def get(self, request):
        return Response(OE.filter(6, 3))
class FilterOrder(APIView):
    def get(self, request, state):
        return Response(OE.filter(state+1, state-1))

class OrderManager:
    def getOrderDetail():
        return OrderDetail
    def getOrderList():
        return OrderList
    def changeState():
        return OrderDetail
    def getCookList():
        return CookOrder
    def getDeliveryList():
        return DeliveryOrder
    def filterOrder():
        return FilterOrder
