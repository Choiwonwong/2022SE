from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .InventoryEntity import InventoryEntity as IE

class GetInventoryList(APIView):
    def get(self, request):
        return Response(IE.getlist())

class EditInventory(APIView):
    def patch(self, request, id):
        count = request.data['count']
        state, response = IE.edit(id, count) # request 객체는 함수 인자로 넘어가면 안됨 -> 3계층으로 넘어가면 안됨
        if state:
            return Response(response)
        else:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class WarnInventory(APIView):
    def get(self, request):
        return Response(IE.warnlist())

class AcceptInventory:
    def reflectInventory(order_id, orderDetail):
        data = orderDetail
        for i in range(len(orderDetail)):
            menu, count = data[i].get("menu"), data[i].get("count") # 메뉴 id와 개수를 하나씩 빼서, 하나씩 변경하자.
            IE.edit(menu, -count, False)
        print("{}번째 주문에 대한 재고 반영 완료".format(order_id))

class InventoryManager:
    def getInventorylist():
        return GetInventoryList
    def editInventory():
        return EditInventory
    def alertInventoryWarn():
        return WarnInventory
    
