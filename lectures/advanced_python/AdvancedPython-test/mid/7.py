print("==========7번 문제==========")
a = input("첫번째 숫자를 입력하세요:")
b = input("두번째 숫자를 입력하세요:")

c = str(int(a)+int(b))
print(c[:-3]+","+c[-3:])