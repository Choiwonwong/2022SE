from rest_framework import serializers
from .models import CustomerAccount, CustomerRank
from .models import Inventory
from .models import Order, OrderDetail, Menu

class MenuSerializer(serializers.ModelSerializer): # 메뉴를 제공할 때 필요한 직렬화기 -> 지금은 안쓰임
    class Meta:
        model = Menu
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer): # 주문 상세를 생성할 때 필요한 직렬화기
    class Meta:
        model = OrderDetail
        fields = ['order_id', 'dinner', 'menu', 'count']

class OrderSerializer(serializers.ModelSerializer): # 주문을 생성, 주문 상태 변경할 때 필요한 직렬화기
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailListSerializer(serializers.ModelSerializer): # 주문 상세를 제공할 때 필요한 직렬화기
    dinner = serializers.CharField(source = "dinner.name")
    style = serializers.CharField(source = "dinner.style.name")
    menu = serializers.CharField(source = "menu.name")
    class Meta:
        model = OrderDetail
        fields = ['order_id', 'dinner', 'style', 'menu', 'count']

class OrderListSerializer(serializers.ModelSerializer): # 주문현황을 제공하기 위한 직렬화기 -> 여기에서 주문 상세가 필요할까? -> 고객 측면에서 주문 현황에서 상세를 확인할 수 있으면 좋고, 직원 측면에서도 주문 현황에서 이를 표시해주면 좋음.
    order_detail = OrderDetailListSerializer(read_only = True, many = True) # 일단 주문 상세는 보내고 보자.
    state = serializers.CharField(source = 'state.name')
    class Meta:
        model = Order
        fields = '__all__'

class RankSerializer(serializers.ModelSerializer): # 등급에 대한 할인값을 가져오고 등급을 수정할 때 필요한 직렬화기
    class Meta:
        model = CustomerRank
        fields = '__all__'

class CustomerRankSerializer(serializers.ModelSerializer): # 고객 등급을 수정할 때 필요한 직렬화기
    class Meta:
        model = CustomerAccount
        fields = ['pk', 'email', 'name', 'address','rank']

class CustomerSerializer(serializers.ModelSerializer): # 직원과 고객에게 고객 정보를 제공할 때의 직렬화기
    order = OrderListSerializer(read_only = True, many = True)
    rank = serializers.CharField(source = 'rank.name')
    class Meta:
        model = CustomerAccount
        fields = ['id','email', 'order', 'name', 'address', 'phone_number', 'rank'] 

class InventorySerializer(serializers.ModelSerializer): # 재고 현황을 제공할 때 사용하는 직렬화기
    class Meta:
        model = Inventory
        fields = '__all__'

class InventorywarnSerializer(serializers.ModelSerializer): # 재고를 경고할 때 사용하는 직렬화기
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'count']


