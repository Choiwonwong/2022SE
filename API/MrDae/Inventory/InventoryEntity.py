from ..models import Inventory
from ..serializers import InventorySerializer, InventorywarnSerializer

class InventoryEntity:
    # 재고 현황을 DB에서 가져와서 직렬해서 데이터를 제공
    def getlist():
        query_set = Inventory.objects.all()
        return InventorySerializer(query_set, many=True).data

    def warnlist():
        warning_set = Inventory.objects.filter(count__lt=10).values('name','count')
        return InventorywarnSerializer(warning_set, many=True).data

    # DB에서 바꿀 객체럴 가져온 다음(obj 변수가 갖는 값) -> request로 들어온 JSON을 수정하고 역직렬화 해서 수정.
    def edit(inventoryid, count, output = True):
        flag = False
        obj = Inventory.objects.get(id=inventoryid)
        temp = InventorySerializer(obj).data.get('count')
        changed_count = temp + count
        serialized = InventorySerializer(obj, data = {'count': changed_count}, partial = True) # 이렇게 지정해서 data를 넘기면 새로운 역직렬화 데이터 생성
        if serialized.is_valid():
            flag = True
            serialized.save()
            response = serialized.data 
        else:
            response = serialized.errors
        if output:    
            return flag, response 
