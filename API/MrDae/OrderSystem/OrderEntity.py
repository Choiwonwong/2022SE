from ..models import Order, OrderDetail
from ..serializers import OrderSerializer, OrderDetailSerializer, OrderListSerializer, OrderDetailListSerializer

from ..CustomerArtifacts.CustomerManager import CustomerRankManager as CRM
from ..Inventory.InventoryManager import AcceptInventory as AI

class OrderEntity:
    def get(customerID, customer_order_id):
        obj = Order.objects.filter(customerid=customerID).get(customer_orderid = customer_order_id)
        return OrderListSerializer(obj).data
    
    def getDetail(orderID):
        obj = Order.objects.get(id = orderID)
        return OrderListSerializer(obj).data

    def getlist(customerID = None): # 특정 고객의 주문 목록 반환
        if customerID is not None:
            query_set = Order.objects.filter(customerid=customerID)
        else:
            query_set = Order.objects.all()
        return OrderListSerializer(query_set, many=True).data

    def add(customerID, orderinfo, price): # 특정 고객의 주문 등록 - 이때 주문정보는 만들어지고 주문 상세까지 함께 만들어져야함.
        discounted_price = CRM.getDiscount(customerID, price) # 등급에 맞는 할인률 요청
        obj = Order.objects.filter(customerid=customerID).order_by("-id").first()
        customer_order_id = OrderSerializer(obj).data.get('customer_orderid')

        data = orderinfo
        data['customerid'] = customerID
        data['price'] = price - discounted_price
        data['discount'] = discounted_price
        if customer_order_id is None: 
            data['customer_orderid'] = 1
        else:
            data['customer_orderid'] = customer_order_id + 1
        serialized = OrderSerializer(data = data)
        if serialized.is_valid():
            serialized.save()
            return serialized.data.get('id'), serialized.data.get('customer_orderid')

    def changeState(orderID):
        flag = False
        obj = Order.objects.get(id = orderID)
        state = OrderSerializer(obj).data.get('state')
        if state >= 6:
            return flag, "해당 주문은 배달완료되었습니다."
        else:
            state = state + 1
        serialized = OrderSerializer(obj, data = {'state': state}, partial= True)
        if serialized.is_valid():
            flag = True
            serialized.save()
            return flag, OrderListSerializer(obj).data    
        else:
            return flag, serialized.errors

    def filter(state, gap = 0):
        obj = Order.objects.filter(state__lt=state) & Order.objects.filter(state__gt=gap)
        return OrderListSerializer(obj, many=True).data

    def delete(orderID):
        obj = Order.objects.get(id=orderID)
        obj.delete()
        print("잘못 입력된 {}번째 주문을 삭제합니다.".format(orderID))

class OrderDetailEntity:
    def get(customerID, orderID):
        obj = OrderDetail.objects.filter(order_id=orderID)
        return OrderDetailListSerializer(obj, many=True).data

    def add(orderID, order_detail):
        for i in range(len(order_detail)):
            order_detail[i]["order_id"] = orderID
        serialized = OrderDetailSerializer(data=order_detail, many=True)
        if serialized.is_valid():
            serialized.save()
            AI.reflectInventory(orderID, order_detail) # 주문에 따른 재고 반영
            return OrderListSerializer(Order.objects.first()).data

