def print_string(text, count=1): #기본값 매개변수가 여러개 쓸 수 있는데, 그럴 때는 좀 다름.
    #기본 값 매개변수는 항상 뒤에 와야함.
    for i in range(count):
        print(text)

print_string("안녕하세요")
print_string("안녕하세요", 2)

def print_string2(text, count=1, c2=10):
    print(text, count, c2)

print_string2("bye", c2 = 10)
#count는 기본값으로 하고 c2 =10 처럼 c2만 할당하고 싶을 때. 키워드 매개변수를 같이 써줘야함. 매개변수 중에 몇개만 바꾸고 싶을 떄.


#print(sum(1,2,3,4,5)) 이러면 안되지. 리스트 함수니까
a = [1,2,3,4,5]
print(sum(a))

def mySum(*num): #sum 함수 쓰지 않고 sum함수 만드는 것임
    Sum =0
    for i in range(len(num)):
        Sum += num[i]
    print(Sum)

def mySum(*num):
    total = 0
    for n in num:
        total +=n
    return total #return을 써야 우리가 쓰는 sum 함수랑 똑같은거지

def mySum2(num_list):
    total =0
    for i in num_list:
        total+=i
    return total

def Up(*words):
    list = []
    for i in range(len(words)):
        list.append(words[i])
    for i in list:
        i = i.upper()
        print(i)


def dic_maker(**pos):
    print(pos)

dic_maker(love = "verb", ant="noun") #{'love':'verb', 'ant':'noun'}, key가 
#딕셔너리인데 =으로 만들잖아. 글자에 값을 어떻게 할당해. 못하니까, 애는 일종의 값 할당이라고 생각하고 쓰는 것.
#오히려 스트링으로 표시하면 안됨.. 에러남.

def hello_k():
    print("안녕하세요")
def hello_e():
    print("Hello")

def greeting(A):
    A() #오 그럼 리턴해주지 않아도 호출할 함수에 리턴 있으면 리턴되겠네??
greeting(hello_k)
greeting(hello_e)


