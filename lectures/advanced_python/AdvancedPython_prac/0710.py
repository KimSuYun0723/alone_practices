def Read(file):
    f = open(file, "r")
    data = f.read()
    f.close() ##필수
    return data

def process(data):
    data0 = data.split("\n")

    for i in data0:
        #name  = i.split(" - ")[0] #굳이? 그냥 스페이스로 나눈거니까 한꺼번에 해도 되잖아
        a = i.replace(",", "")
        score = a.split(" ")
        name = score[0]
        Korean = int(score[score.index("Korean:")+1]) #벨류 값을 딕셔너리로 하는 딕셔너리 만들면 좀 편하지 않겠어?
        English = int(score[score.index("English:")+1])
        Math = int(score[score.index("Math:")+1])
        av = (Korean+English+Math)/3 #len으로 해야지;;;;=> 딕셔너리에서 value값을 리스트로 받으면 할 수 있잖아
        line = f"{name}: {av}"
        print(line)

data = Read("score.txt") #점수가 1의 자리, 3자리, 소수점자리도 있을 수 있는거잖아?
process(data)

#너무 큰 데이터에서는 오류 하나 있으면 그걸 잡긴 힘듦. 그러면 자연어처리가 100%겠지..



"""
1.
Emma - Korean: 
68, English: 
41, Math: 
83 
,를 만나거나 " "를 만나기 전 인덱스..

2. ,로 스플릿
Emma - Korean: 68,
 English: 41,
 Math: 83

어떤건 막 스페이스 2개거나 스페이스 없거나 막 그런게 있는데, 
그런건 결국에 정규 표현식가지고 하는 것..
"""


def print_string(text, count=1):
    for i in range(count):
        print(text, count)

#def print_string(text, num=100, count=1): -> count만 바꾸고 싶어도 num=100을 알려줘야 기본값 매개변수 사용가능...

"""
키워드 매개변수가 그러헥 나옴
-> 호출할떄!!!!!! 중요
-> 호출할 때 키워드 달고 나오는게 중요
-> 자리를 찾아가지 않고, 변수 이름 따라 입력하니까 순서 바뀌어도 ㄱㅊ
-> 단점은 타이핑을 해야한다는 점

기본값 여러개 중에, 딱 하나만 바꾸고 싶다거나.. 그런것들. reverse라던가..
"""

print_string("abc")

def print_personnel(name, age, nationality):
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"nationality: {nationality}")

print_personnel("kim", 3, "KOR")

def print_POS(**words):
    for i in range(len(words)):
        print(f"{list(words.keys())[i]}:{list(words.values())[i]}")

print("#######################")
print_POS(love = "love")
#print_POS('love'='love') #key가 스트링이어도 따옴표 붙이면 안됨. string에다가 값을 할당하는건 말이 안되니까
print("#######################")
print_POS(love='verb', computer='noun', paper='noun', pretty='adjective')


