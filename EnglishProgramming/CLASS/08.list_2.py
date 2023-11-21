#del (리스트 변수)[인덱스]
"""
    : 인덱스 번호로 삭제하는 예약어
- 사실 함수는 아님. (문법도 다름)
- 변수할당 안됨  ##n_fruit = del fruit[0] --> error
- 원본 훼손
-> 훼손시키는 함수들은 대체로 아무것도 반환 X
"""
print("========== del ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
#n_fruit = del fruit[0] -->error
del fruit[0]
print(fruit)



#리스트변수.remove(지울 값)
"""
    : 값을 이용하여 삭제하는 함수
- 여러 개의 값이 있어도 가장 처음 발견된 요소만 삭제
- replace는 match되는 패턴 여러개에 다 해당되지만, remove는 아님.
- 원본 훼손
- 변수에 담았을 때, 에러는 안나지만 None값.(할당이 안됨)
"""
print("========== remove ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
a = fruit.remove("apple") #None
print(a)



#리스트변수.pop(인덱스 번호)
"""
    : 리스트 마지막 요소 or 인덱스 번호로 요소 반환 & 삭제
- 원본 훼손(but 할당가능)
"""
print("========== pop ==========")
#1
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
fruit.pop() # 마지막 요소 반환 -> 할당도 가능
print(fruit)

#2
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
k = fruit.pop(1) # orange 반환 -> 할당도 가능
print(k)
print(fruit) #orange



#리스트변수이름.clear()
"""
    : 리스트 안의 모든 요소 삭제
- 원본데이터 훼손
- 할당시 에러는 안나지만 None 값 출력
"""
print("========== clear ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
a= fruit.clear()
print(a) # None
print(fruit) #출력은 되네?
#그냥 fruit = [] 이렇게 요소 삭제도 가능 --> list 형태 유지 ??
### 그럼 clear랑 fruit=[] 랑 차이는 뭐임
### clear() 괄호 안에 뭐들어가는거임?



#slicing : 리스트변수[a:b:c]
"""
    : 문자열 slicing이랑 동일
-  인덱스 2번부터 7번까지 2개마다 등장하는 요소 a[2:8:2]
"""



#slicing_2 : slice(a,b,c) ... 시험에는 안나옴
"""
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = slice(1, 3)
print(a[a1]) or print(a[slice(1,3)])

a2 = slice(0, len(a), 2) or a2 = slice(0, 10, 2)
print(a[a2])
"""



#(문자열변수).split(구분문자)
"""
    : 문자열을 특정한 구분문자로 분할 --> 리스트 형으로
- 구분문자 미지정시 공백이 default.
- 할당 가능
- string --> list
"""



#"연결문자".join(리스트변수)
"""
    : 분할된 것을 결합
- 원본 훼손 X --> 저장하려면 할당 가능
- list --> string
"""
print("========== split&join ==========")
s1 = "This is a computer"
s2 = "2023/03/01"

s1_2 = s1.split()
print(s1) #This is a computer
print(s1_2) #['This', 'is', 'a', 'computer']

s3 = " ".join(s1_2)
print(s1) #This is a computer
print(s1_2) #['This', 'is', 'a', 'computer']
print(s3) #This is a computer 
# 할당해야 출력이 되는구만..

s2_2 = s2.split("/")
print(s2)
print(s2_2)

s4 = "/".join(s2_2)
print(s2)
print(s2_2)
print(s4)
print(type(s4))



#(리스트변수).count(빈도찾고자하는 값)
"""
    : 리스트에서 특정 값 x의 빈도 구하는 함수
- "빈도 찾고자 하는 값"이 완전히 일치해야 구할 수 있음.
"""
print("========== count ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
print(fruit.count("apple"))
n_apple = fruit.count("apple") #언더바로 시작하면 변수 안되나?



#리스트변수.sort()
"""
    : 리스트 오름차순 정렬 #내림차순: a.sort(reverse = True)
- 원본 훼손.
- 할당 시, 에러는 안나지만 None(할당 불가)
- 리스트 안에 num, str 같이 있으면 쓸 수 X
"""
print("========== sort ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
fruit.sort()
print(fruit)
#새로운 변수에 담고자 한다면…?
n_fruit = fruit.sort() 
print(n_fruit) #error X, but None



# sorted(리스트변수)
"""
    : 리스트 오름차순 정렬 # 내림차순: sorted(a, reverse = True)
- 원본유지
- 정렬한 데이터는 반드시 변수에 할당.
- 정렬 순서 : 공백 -> 숫자 -> 대문자 -> 소문자
"""
print("========== sorted ==========")
fruit = ["apple", "orange", "apple", "strawberry", "kiwi"]
sorted(fruit)
print(fruit) #원본 순서 바뀌지 않음
n_fruit = sorted(fruit) #정렬한 데이터는 반드시 새로운 변수에 담아야만 함!
print(n_fruit)



#튜플
"""
- 요소 값 변경 불가 --> 내장함수가 별로 없음
• 튜플 a 만들기 (빈 튜플)
• 요소: 10, 20, 30, 40 넣기
• 첫번째 인덱스 값 구하기
• 슬라이스 해보기 a[:2]
• 튜플 안의 요소 추가 삭제 바꾸기 등 해보기
• a[0] = 50
"""
print("========== tuple ==========")
a = (10, 20, 30, 40)
print(a[0]) #10 인덱싱 가능
z = a[:2]
print(z) #(10,20) 슬라이싱 가능
#a[0] = 0  #TypeError --> 요소가 고쳐지지 않음.
print(a)

b = (100, 200)
a += b #오 이건 가능하네?
print(a)
print(b)



#list(), tuple() : 튜플 <-->리스트 변환

#진짜 실습