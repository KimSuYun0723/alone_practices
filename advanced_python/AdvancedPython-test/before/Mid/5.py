#!/usr/bin/env python3

print("---5번 문제---")

coffee = {"아메리카노": 3500, "카페라떼": 4000, "카페모카": 4500, "카푸치노": 4000}
food = {"햄샌드위치": 7500, "치킨샌드위치": 8000, "크로플": 5500}

table_num = input("테이블 번호를 입력하세요: ")
menus = []
while True:
	menu = input("메뉴를 입력하세요: ")
	if menu == "종료":
		break
	menus.append(menu)

print("---5-1번 문제---")

result = 0
index = 0
while index < len(menus):
	if menus[index] in coffee:
		result += coffee[menus[index]]
	else:
		result += food[menus[index]]
	index += 1

print(f"{table_num}번 테이블: {result}원")

print("---5-2번 문제---")

result = 0
index = 0
coffee_price = []
coffee_num = 0
food_num = 0
while index < len(menus):
	if menus[index] in coffee:
		coffee_price.append(coffee[menus[index]])
		coffee_num += 1
	else:
		result += food[menus[index]]
		food_num += 1
	index += 1
	
coffee_price.sort(reverse = True)
if coffee_num != 0 and food_num != 0:
	index = 0
	while index < food_num:
		coffee_price[index] = coffee_price[index] / 2
		result += coffee_price[index]
		index += 1

print(f"{table_num}번 테이블: {int(result)}원")
