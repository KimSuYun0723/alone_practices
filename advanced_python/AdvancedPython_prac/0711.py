
def Sum(a1,a2):
    result = a1+a2
    print(result)

def minus(a1,a2):
    result = a1-a2
    print(result)

def gop(a1,a2):
    result = a1*a2
    print(result)

def divide(a1,a2):
    result = a1/a2
    print(result)

def call_cal(a1,a2,func):
    func(a1,a2)
    #return func(a1,a2)

call_cal(1,2,Sum)

"""
각각의 함수를 return이라고 하고(지금은 print),
a = call_cal(1,2,Sum) 
print(a)
라고 하면 None 출력.
왜냐면 call_cal 이라는 함수엔 return이나 print가 없기 때문에
"""

def cal(a,b, op):
    def cal_plus():
        return a+b
    def cal_minus():
        return a-b
    
    if op == "plus":
        print(cal_plus())
    elif op == "minus":
        print(cal_minus())

cal(1,2,"plus") #이런식으로 바깥에서 중첩함수 호출할려면 if문으로 함수안에서 정의

############################################################################

def personal_info(file, answer):
    #파일 읽는 함수
    def Read(file):
        f = open(file, "r")
        info = f.read()
        f.close()
        return info

    #원하는 데이터 찾는 변수
    def GetData(data, answer):
        data= data.replace("\n\n", ": ").replace("\n", ": ")
        List =[]
        data0 = data.split(": ")

        if answer == "이름":
            for i in data0:
                if i =="Name":
                    ans = data0[data0.index(i)+1]
                    List.append(ans)
                    data0.pop(data0.index(i)+1)

        elif answer == "나이":
            for i in data0:
                if i =="Age":
                    ans = data0[data0.index(i)+1]
                    List.append(ans)
                    data0.pop(data0.index(i)+1)

        elif answer == "학번":
            for i in data0:
                if i =="Student_id":
                    ans = data0[data0.index(i)+1]
                    List.append(ans)
                    data0.pop(data0.index(i)+1)

        elif answer == "지역":
            for i in data0:
                if i =="Location":
                    ans = data0[data0.index(i)+1]
                    List.append(ans)
                    data0.pop(data0.index(i)+1)

        elif answer == "전화번호":
            for i in data0:
                if i =="Phone":
                    ans = data0[data0.index(i)+1]
                    List.append(ans)
                    data0.pop(data0.index(i)+1)
        print(List)

    data = Read(file)
    GetData(data, answer)

a = str(input("원하는 정보를 말씀해주세요: "))
personal_info("Personal_info.txt", "이름")
personal_info("Personal_info.txt", "나이")

#############################

import calendar
calendar.calendar(2022) #print 내장 X
calendar.prmonth(2022,7) #print 내장
a = calendar.monthrange(2022, 7) #print 내장 X
print(a)

import random
random.random() #: 0~1사이 실수 중 난수
random.randint("시작값, 끝값")

import math
print(math.pi)

"""
• 문법 1
import 모듈이름
모듈이름.함수()
• 문법 2
• from 모듈이름 import 변수 또는 함수
• 함수()

"""


import random
c = [1,2,3,4,5]
d = random.shuffle(c)
print(d) #None
print(c) #원본이 훼손되는 함수는 이렇게

#import calculator.cal
#print(calculator.cal.plus(1,2))
"""
내가 지금 존재하는 파일 위치를 기준으로 "폴더나 파일이 어디까지 보이는지"
import calculator.cal as cc
a = cc.plus(1,2)
print(a)
-> 시험에는 안나온대~
"""


#from calculator.cal import plus, minus, divide, ~~

#import calculator
"""패키지를 쓰고 만드는건 시험에 못내, 함수는 personal info~ 기존 코드를 함수로 바꾸면 어떻게? 
중첩함수로 하려면 어떻게 해야 하지? 문제는 숫자, 문자도 나오지만 문자도 나오는데 문자열 자체를 처리하는건 안내고
반복문, 조건, 함수 니까 문자는 들어있지만 문자열 자체를 처리하는건 잘 안낼거고
글자 텍스트를 주고 이렇게 하세요 그런건 안낼 예정"""