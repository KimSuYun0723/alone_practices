#1. type(), 연산자
a = 3+2j
b = -1
c = 3+2j
print(type(type(a))) #<class, 'type'> 
    #==> type()의 type은 'type'
print(type(3+2j)) #<class, 'complex'>
print(type(b)) #<class, 'int'>
print(type(7/5)) #<class, 'float'>
print(type(6/3)) #<class, 'float'>
print(type(7//5)) #<class, 'int'>
print(type(6//3)) #: 몫의 소수점을 버린 것 #<class, 'int'>
print(type(6%3)) #<class, 'int'>
print(type(2**30)) #<class, 'int'>


#2. 부동 소수점(지수표기 방식)
a = 1.23e2
b = 1.23e2
print(a+b)
print(type(a+b)) #<class, 'float'>

g = 1.35e-10
h = 2.46e-10
print(g+h)
print(type(g+h))
print(g-h)
print(type(g-h))
print(g*h)
print(type(g*h))
print(g/h)
print(type(g/h))
print(g//h) #0.0
print(type(g//h))
#전부 <class, 'float'>

#int(): 뒤를 버림
# round(): 반올림
k =3
m = 3/1
print(k,m,type(m))

#3.complex num
a = 2+3j
a.real #a에서 실수부 꺼내서 ==> 대체로 .을씀
#float
a.imag
#float
a.conjugate() #켤레복소수, 뒤에 괄호 붙음
#(2-3j) : 이렇게 튜플로 나오는 것임. j가 변수일 수도 있잖아?

#=============================================실습========================================

#1. 12345초는 몇시간 몇분 몇초인가?
a = 12345
rest = a%60
min = a//60
hour = min//60
min = min%60
print("=================================실습1=================================")
print(f"{hour}시간 {min}분 {rest}초")


"""2. 
• 어느 꽃집의 장미 가격은 1송이 5000원, 튤립 1송이 6500원, 해바라기 1송이
4200원이고, 6월 한정 세일로 10% 할인을 해준다. 아래 test 1 ~ 3번을 계산하고
손님이 지불해야할 금액을 출력하세요. 
• test1: 장미 5송이, 튤립 2송이를 구매했을 때 총액은? 34200
• test2: 튤립 10송이를 구매했을 때 총액은? 58500
• test3: 장미 3송이, 튤립 3송이, 해바라기 3송이를 구매했을 때 총액은? 42390
• 필요한 변수를 만들고 총액은 print 함수를 이용하여 각각 출력하세요.
"""

print("=================================실습2==================================")
rose = 5000
tulip = 6500
sunflower = 4200
sale = int(input("몇 % 세일인가요? : "))
n=1

while True:
    ask = str(input("꽃 사시겠습니까? => 네/아니요/글쎼요 : "))
    if ask == "아니요":
        break

    elif ask == "네":
        Rnum = int(input("장미 몇송이 사시겠습니까? : "))
        Tnum = int(input("튤립 몇송이 사시겠습니까? : "))
        Snum = int(input("해바라기 몇송이 사시겠습니까? : "))
        total = (rose*Rnum + tulip*Tnum + sunflower*Snum)*(100-sale)/100
        print("test", n, int(total), "원")
        print("==============================================")
        n+=1

    elif ask == "글쎄요":
        print("둘러보시고 다시 불러주세요.")

    else:
        print("잘못 누르신 것 같습니다. 다시 시도하세요.")

#언제는 튤립이 잘팔리고, 언제는 쟤가 잘팔리네~?
#10의자리에서 올림하는 것은 어떻게??(동전에 1원이 없응께)

#3. input
"""
- input으로 받는거 자료형 변환안해주면 항상 string
1=> '1'
에러뜸...
"""
num1 = input("입력: ") #1
num2 = input("입력: ") #2
print(num1+num2) #12

"""
int(input)을 하고 싶으면,
입력받을때부터 int 씌우지 말고
결과값 계산할때 결과값에 씌우던지, 구할때 씌우던지.
왜냐면 처음부터 int가 아니면 error가 생기기 때문에,
예외처리도 안됨;;;
input 쓸 때 뉴라인 쓰면 좀 예쁨
"""
#a.isdecimal() : 글자로 들어온 애중에, 숫자로 바꿀수 있는지 알려주는 애(글자 아니면 error)
#a.isdigit()

#문자열

print("===============실습1==============")
print("오늘은 \"날씨\"가 좋네요. 내일도 \"날씨\"가 좋다고 합니다.")
#이스케이프 시퀀스/ '로 묶기 / """로 묶기

print("===============실습2==============")
print('오늘은 "날씨"가 좋네요. \n내일도 "날씨"가 좋다고 합니다.')