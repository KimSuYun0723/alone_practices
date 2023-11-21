def your_name(*name):
    if len(name) ==1:
        print(name[0])
    else:
        print(" ".join(name))

your_name("김수윤")
your_name("김수윤", "김송현")


#실습1
def ur_fav_col(*col):
    num = len(col)
    print(f"you like {num} different colors") #그냥 바로 len(col)해도 되지


def ur_fav(what, *ex):
    num = len(ex)
    if what == "color":
        print(f"You like {num} different colors.")
    elif what == "animal":
        print(f"You like {num} different animals.")
    else:
        print(f"You like {num} different things.")

#교수님 버전
def ur_fav(what, *things):
    print(f"You like {len(things)} different {what}(s).")
ur_fav("animal", "dog", "cat")

#함수를 미지수에 담기
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b

p = plus
p(1,2)
m = minus
m(5,1)

cal = [plus, minus] #cal 리스트에 함수 이름을 넣음
cal[0](1, 2) #cal[0]이 plus를 대신함
cal[1](5, 1) #cal[1]이 minus를 대신함

#Others
def hello_k():
    print("안녕하세요")
def hello_e():
    print("Hello")
def greeting(A): #greeting이라는 함수는 함수를 호출하는 함수(호출하는 함수를 따로만들고 싶다! 하면 사용가능)
    A()
greeting(hello_k) #매개변수 자리에 함수이름을 인수로 입력함
greeting(hello_e)

#중첩함수
def cal(a, b):
    def cal_plus (): #a,b 안써도 괜찮음 이럴떄는
        return a+b
    def cal_minus ():
        return a-b
    print(cal_plus())
    print(cal_minus())
cal(4, 1)

#중첩된 함수는 함수 밖에서는 호출 불가
#cal(4, 1, cal_plus)불가
#cal_plus()

def cal(a, b, op):
    def cal_plus (a,b): #a,b 안써도 괜찮음 이럴떄는
        return a+b
    def cal_minus (a,b):
        return a-b
    def call_op(op):
        op(a,b)

    if op == "cal_plus":
        print(cal_plus(a,b))
    elif op == "minus":
        print(cal_minus(a,b))
    print(cal_plus()) #이런건 또 에러남. arguments 2개 없다고
    print(cal_minus())
    print(call_op())
cal(4, 1, "cal_plus")

