#type() : 입력값의 자료형 알려줌.
print("==========type()===========")
a= 1234
b=3.1415
c=3+4j
f= -3
type(a)
type(b)
type(c)
type(a-f)

#int : 파이썬에서는 메모리가 허용하는 한 무한대 정수 다루기 가능
print("==========연산자==========")
x=5
y=3
print(x/y) #몫
print(x//y) #몫의 소수점 이해 버림
print(x%y) #나머지

#float :실수
k = 22/7 #22/7=무리수, 소수점 이하 15자리까지만 표현
print("===========무리수 type==========")
type(k)

#복소수(complex) : 파이썬에서는 허수 단위를 나타내는 부호로 i대신 j씀
print("==========complex============")
a = 2+3j
a
type(a)
a.real #2.0 : 실수부분
a.imag #3.0 : 허수부분
a.conjugate() #2-3j : 켤레 복소수

#실습
print("===========실습===========")
ame_price = 3500
cafe_price = 4000
ame = 2
cafe = 2

total1 = ame_price*ame+cafe_price*cafe
print(total1)

ame_price = 3500
va_price = 4300
ain_price = 5000
ame = 3
va = 4
ain = 2

total2 = int((ame_price*ame+va_price*va+ain_price*ain)*90/100)
print(total2)