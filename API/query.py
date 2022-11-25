import sqlite3
conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

"""
Inventory 데이터 입력
id, name, count, threshold
"""
# 기존 하나씩 추가해보던 데이터 삭제 위해 DELETE 연산 수행
c.execute("DELETE FROM MrDae_inventory")
Inventory_query = "INSERT INTO MrDae_inventory VALUES (?, ?, ?)"
c.execute(Inventory_query, (1, '스테이크', 30))
c.execute(Inventory_query, (2, '와인', 30))
c.execute(Inventory_query, (3, '커피', 30))
c.execute(Inventory_query, (4, '샴페인', 30))
c.execute(Inventory_query, (5, '샐러드', 30))
c.execute(Inventory_query, (6, '애그 스크렘블', 20))
c.execute(Inventory_query, (7, '베이컨', 30))
c.execute(Inventory_query, (8, '빵', 30))
c.execute(Inventory_query, (9, '바게트빵', 30))


"""
customerType 데이터 입력
couponID, type, discount
"""
# 기존 하나씩 추가해보던 데이터 삭제 위해 DELETE 연산 수행
c.execute("DELETE FROM MrDae_customerrank")
CustomerType_query = "INSERT INTO MrDae_customerrank VALUES (?, ?, ?, ?)"
c.execute(CustomerType_query, (0, '방문한 분', 0, 0))
c.execute(CustomerType_query, (1, '고마운 분', 5, 5))
c.execute(CustomerType_query, (2, '더 고마운 분', 10, 10))
c.execute(CustomerType_query, (3, '많이 고마운 분', 20, 15))


"""
Style 데이터 입력 
id, name, dish, napkin, cup, tray
"""
c.execute("DELETE FROM MrDae_style")
Style_query = "INSERT INTO MrDae_style VALUES (?, ?, ?, ?, ?, ?)"
c.execute(Style_query, (0, '단품', "", "", "", ""))
c.execute(Style_query, (1, '심플 스타일', '상자 접시', '일반 냅킨', '플라스틱 잔', '플라스틱 쟁반'))
c.execute(Style_query, (2, '그랜드 스타일', '도자기 접시', '면 냅킨', '도자기 잔', '나무 쟁반'))
c.execute(Style_query, (3, '디럭스 스타일', '도자기 접시', '린넨 냅킨', '꽃들이 있는 작은 병', '은 쟁반'))

"""
menu 데이터 입력
id, name, price
"""
c.execute("DELETE FROM MrDae_menu")
Menu_query = "INSERT INTO MrDae_menu VALUES (?, ? , ?)"
c.execute(Menu_query, (1, '스테이크', 15000))
c.execute(Menu_query, (2, '와인', 10000))
c.execute(Menu_query, (3, '커피', 2000))
c.execute(Menu_query, (4, '샴페인', 15000))
c.execute(Menu_query, (5, '샐러드', 1000))
c.execute(Menu_query, (6, '애그 스크렘블', 2000))
c.execute(Menu_query, (7, '베이컨', 2000))
c.execute(Menu_query, (8, '빵', 1000))
c.execute(Menu_query, (9, '바게트빵', 3000))

"""
staff 데이터 입력
id, account, password, authority
0 = False, 1 = True
"""
c.execute("DELETE FROM MrDae_staff")
staff_query = "INSERT INTO MrDae_staff VALUES (?, ?, ?, ?)"
c.execute(staff_query, (1, 'staff1', 'staffpw01', False))
c.execute(staff_query, (2, 'staff2', 'staffpw02', False))
c.execute(staff_query, (3, 'staff3', 'staffpw03', False))
c.execute(staff_query, (4, 'staff4', 'staffpw04', False))
c.execute(staff_query, (5, 'staff5', 'staffpw05', False))
c.execute(staff_query, (6, 'staff6', 'staffpw06', False))
c.execute(staff_query, (7, 'staff7', 'staffpw07', False))
c.execute(staff_query, (8, 'staff8', 'staffpw08', False))
c.execute(staff_query, (9, 'staff9', 'staffpw09', False))
c.execute(staff_query, (10, 'staff10', 'staffpw10', False))
c.execute(staff_query, (11, 'staff11', 'staffpw11', True))

c.execute("DELETE FROM MrDae_dinner")
Dinner_query = "INSERT INTO MrDae_dinner VALUES(?, ?, ?)"
c.execute(Dinner_query, (1, '발렌타인 디너', 1))
c.execute(Dinner_query, (2, '발렌타인 디너', 2))
c.execute(Dinner_query, (3, '발렌타인 디너', 3))
c.execute(Dinner_query, (4, '프렌치 디너', 1))
c.execute(Dinner_query, (5, '프렌치 디너', 2))
c.execute(Dinner_query, (6, '프렌치 디너', 3))
c.execute(Dinner_query, (7, '잉글리스 디너', 1))
c.execute(Dinner_query, (8, '잉글리스 디너', 2))
c.execute(Dinner_query, (9, '잉글리스 디너', 3))
c.execute(Dinner_query, (10, '샴페인 축제 디너', 2))
c.execute(Dinner_query, (11, '샴페인 축제 디너', 3))
c.execute(Dinner_query, (99, '단품', 0))

c.execute("DELETE FROM MrDae_orderstate")
OrderState_query = "INSERT INTO MrDae_orderstate VALUES(?, ?, ?)"
c.execute(OrderState_query, (1, 1, '주문 접수'))
c.execute(OrderState_query, (2, 2, '요리 대기'))
c.execute(OrderState_query, (3, 3, '요리 중'))
c.execute(OrderState_query, (4, 4, '배달 대기'))
c.execute(OrderState_query, (5, 5, '배달 중'))
c.execute(OrderState_query, (6, 6, '배달 완료'))

conn.commit()

c.close()
conn.close()

"""
Dinner 데이터 입력
dinnerID, name

Dinner_query = "INSERT INTO Dinner VALUES(?, ?)"
c.execute(Dinner_query, ('D01', '발렌타인 디너'))
c.execute(Dinner_query, ('D02', '프렌치 디너'))
c.execute(Dinner_query, ('D03', '잉글리스 디너'))
c.execute(Dinner_query, ('D04', '샴페인 축제 디너'))
"""
