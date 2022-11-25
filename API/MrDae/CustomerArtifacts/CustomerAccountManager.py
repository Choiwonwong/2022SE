from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .CustomerAccountEntity import CustomerAccountEntity as CA
from MrDae import processing

class CustomerAccountDetail(APIView):
    def get(self, request): # 고객용
        try: 
            customer_id = processing.getUserID(request.COOKIES)
            return Response(CA.get(customer_id))
        except:
            return Response("Not Login", status=status.HTTP_400_BAD_REQUEST)
            
    def patch(self, request):
        try: 
            customer_id = processing.getUserID(request.COOKIES)
            user_info = CA.get(customer_id)
            changed_info = processing.getUserInfo(request.data, user_info)
            
            state, response = CA.editInfo(customer_id, changed_info)
            if state:
                return Response(response)
            else:
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Not Login", status=status.HTTP_400_BAD_REQUEST)

class CustomerAccountManager:
    def getAccountDeTail(): # [고객] 단일 고객 계정 요청
        return CustomerAccountDetail
    def editInfo(): # [고객] 단일 고객 정보 변경
        return CustomerAccountDetail
