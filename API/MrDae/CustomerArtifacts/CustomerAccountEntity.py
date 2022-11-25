from ..models import CustomerAccount

from ..serializers import CustomerSerializer
from ..serializers import CustomerRankSerializer

class CustomerAccountEntity:
    def getlist():
        query_set = CustomerAccount.objects.all()    
        return CustomerSerializer(query_set, many=True).data
        
    def get(customerID):
        obj = CustomerAccount.objects.get(pk=customerID)
        return CustomerSerializer(obj).data
        
    def editInfo(customerID, Data):
        obj = CustomerAccount.objects.get(pk = customerID)
        serialized = CustomerSerializer(obj, data = Data, partial = True)
        if serialized.is_valid():
            flag= True
            serialized.save()
            response = serialized.data
        else:
            response = serialized.errors
        return flag, response

    def editRank(customerID, rank):
        flag = False
        obj = CustomerAccount.objects.get(pk = customerID)
        data = {'rank': rank}
        serialized = CustomerRankSerializer(obj, data = data, partial = True)
        if serialized.is_valid():
            flag= True
            serialized.save()
            response = serialized.data
        else:
            response = serialized.errors
        return flag, response

    def filter(rank):
        query_set = CustomerAccount.objects.filter(rank = rank)
        return CustomerSerializer(query_set, many=True).data



