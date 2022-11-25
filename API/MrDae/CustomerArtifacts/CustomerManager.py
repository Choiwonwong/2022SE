from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .CustomerAccountEntity import CustomerAccountEntity as CA

from ..models import CustomerRank
from ..serializers import RankSerializer

class AccountDetail(APIView):
    def get(self, request, customerid): # 직원용
        try: 
            return Response(CA.get(customerid))
        except:
            return Response("[URL ERROR]{}번째 계정은 존재하지 않습니다.".format(customerid), status=status.HTTP_404_NOT_FOUND)

class AccountList(APIView):
    def get(self, request):
        response = CA.getlist()
        return Response(response, status=status.HTTP_200_OK)

class AccountFilter(APIView):
    def get(self, request, rank):
        try:
            return Response(CA.filter(rank))
        except:
            return Response(CA.filter(0))

class CustomerManager:
    def getCustomerDetail():
        return AccountDetail
    def getCustomerList():
        return AccountList
    def filterCustomerRank():
        return AccountFilter 

class CustomerRankManager:
    def getDiscount(customerID, price):
        rank = CA.get(customerID)['rank']
        obj = CustomerRank.objects.get(name=rank)
        discount = RankSerializer(obj).data['discount']
        discounted_price = int(price * (discount/100)) # 할인된 금액 계산
        return discounted_price

    def updateRank(customerID, customerRank):
        order = CA.get(customerID)['order']
        order_count = len(order) # 이 고객의 주문 개수
        rank_condition = int(order_count/5) * 5 # 주문 개수를 5배수로 변환
        if rank_condition > 15: return # 주문 개수 15번 넘으면 실행 X

        obj = CustomerRank.objects.get(condition = rank_condition) # 이 고객의 주문개수에 맞는 등급 객체 반환
        serialized = RankSerializer(obj).data # 등급 객체 직렬화
        if customerRank == serialized['name']: # 기존 등급과 현 등급이 같으면 종료
            return
        else: # 기존 등급과 현 등급이 다르면 기존 등급을 현 등급으로 수정
            CA.editRank(customerID, serialized['id'])
            print("{}번째 고객 등급 상승! {} >>>> {}".format(customerID, customerRank, serialized['name']))