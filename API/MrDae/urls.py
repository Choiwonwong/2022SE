from django.urls import path
from .Inventory.InventoryManager import InventoryManager as IM
from .CustomerArtifacts.CustomerAccountManager import CustomerAccountManager as CAM
from .OrderSystem.OrderReceptManager import OrderReceptManager as ORM
from .CustomerArtifacts.CustomerManager import CustomerManager as CM 
from .OrderSystem.OrderManager import OrderManager as OM


urlpatterns = [
    path('customers/', CM.getCustomerList().as_view()), #[직원][GET] 고객 계정 리스트 요청
    path('customers/<int:customerid>/', CM.getCustomerDetail().as_view()), #[직원][GET] 특정 고객 계정 요청
    path('customers/rank/<int:rank>/', CM.filterCustomerRank().as_view()), # [직원][POST]고객 등급으로 필터링

    path('customerinfos/', CAM.getAccountDeTail().as_view()), # [고객][GET] 고객 정보 조회, [PATCH] 고객 정보 변경

    path('customers/orders/', ORM.makeOrder().as_view()), #[고객][GET] 특정 고객의 주문 리스트 요청, [POST]고객 주문 생성
    path('customers/orders/<int:customer_orderid>/', ORM.getOrderDetail().as_view()), #[고객][GET] 특정 고객의 특정 주문 요청 - 주문상세까지 포함해서 보냄

    path('orders/', OM.getOrderList().as_view()), #[직원][GET] 전체 주문 목록 요청
    path('orders/<int:orderid>/', OM.getOrderDetail().as_view()), #[직원][GET] 특정 주문 요청, [POST] 주문 상태 변경
    path('orders/cook/', OM.getCookList().as_view()), #[직원][GET] 주문 접수 ~ 요리 중까지의 주문 목록 요청
    path('orders/delivery/', OM.getDeliveryList().as_view()), #[직원][GET] 배달 대기 ~ 배달 중까지의 주문 목록 요청
    path('orders/search/<int:state>/', OM.filterOrder().as_view()), #[직원][GET] 특정 상태의 주문 목록 요청

    path('inventories/', IM.getInventorylist().as_view()), # [직원][GET] 재고 리스트 요청
    path('inventories/<int:id>/', IM.editInventory().as_view()), #[직원][PATCH] 특정 품목의 재고 수정
    path('inventories/warn/', IM.alertInventoryWarn().as_view()), # [직원][GET] 임계치를 달성한 재고 리스트 반환
]