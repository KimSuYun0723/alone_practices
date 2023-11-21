"""
<python datatypes>
1. numeric -> Integer, Float, Complex No.
2. Dictionary
3. Boolean
4. Set
5. Sequence Type -> Strings, List, Tuple
"""



# (리스트변수).index(값)
# len(리스트) : 요소 개수 반환
print("==========len 함수==========")
list = [1,2,3,4]
a = len(list)
print("a_len_type: ", type(a)) #int


# sum(리스트) : 리스트 합계 계산
"""
    ==> sum 함수 입력값으로 가능한 것은?
    -> +로 묶이는건가봐. str은 묶을 수 없는듯. 숫자만 가능한듯.
"""
print("==========sum 함수==========")
str = ["안녕하세요", "오 대박", "안녕"]
num = [1,2,3,4,5,6]
#p = sum(str) -> TypeError
q = sum(num)
print(q)



##변수 재할당
"""
a=[1,2,3,4,5,"mango"]
b=a ---> X (주소가 똑같아(?))
c=a[:] ---> O 
"""



#리스트에 추가하는 함수들
"""
    ==> 원본 훼손 시키는 함수 => 변수 재할당 X
    => replace는 할당을 시켜야 활용 가능...
"""
print("\n==========kkkkkkkkkk==========")
LIST = "1234567890"
kkk = LIST.replace("3", "100")

print(LIST)
print(kkk)



    #1. (리스트변수).append(추가할 요소)
"""
    : 리스트 마지막 요소 뒤에 요소를 추가 하는 함수
"""



    #2. (기존리스트변수).extend(추가할 리스트)
"""
    : 리스트에 다른 리스트를 추가하는 함수
- extent(t) != append(t) ##요소만 추가됨!!
- 할당 불가
"""
print("========== extend 함수 ==========")
num1 = [1,2,3,4,5,6]
num2 = [1,2,3,4,5,6]
t = [1,2,3]
k= num1.extend(t) 
l= num1.append(t)
print(k,l) #None None

num2.extend(t) #요소만 추가
print(num2) 
num2.append(t) #t라는 리스트 자체가 요소로 추가
print(num2)



    #3. (기존리스트변수).insert(인덱스번호, 추가할 값)
"""
    : 리스트 인덱스 번호를 이용하여 원하는 인덱스 값에 추가
    a.insert(i,x) == 리스트 a의 인덱스 i번에 값 x 삽입
- 할당 에러는 안나지만 None
"""



#리스트의 결합
    #1. +연산자 : 리스트1 + 리스트2
"""
- 문자열 +연산자와 다름
"""
print("==========리스트 + 연산자 ==========")
m = [1,2,3]
n = [4,5,6]
print(m+n) #[1, 2, 3, 4, 5, 6]



    #2. += 연산자 : 
"""
- 리스트에 다른 리스트의 요소를 추가
"""
print("==========리스트 += 연산자 ==========")
m = [10,20,30]
m += [40,50,60]
print(m) #[10, 20, 30, 40, 50, 60]



#복합대입연산자 = 수식연산자+할당연산자
    #중에서도 += --> 숫자, 문자열, list 사용 가능. list는 += 만 가능?
