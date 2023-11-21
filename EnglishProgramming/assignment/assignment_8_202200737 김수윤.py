"""
def 실습
• data: emily.txt
• 사용자 정의 함수 만들 것
1. 파일 열고 읽는 함수
2. 단어목록을 만들고 출력하는 함수
3. 문장목록을 만들고 출력하는 함수
• return/print는 자유롭게 & 다양하게 연습하면서 만들어 보세요.
"""

data = str(input("데이터 경로를 넣어주세요: "))

def Read(data):
    f = open(data, "r")
    Use = f.read() 
    f.close()
    return Use

def Word(paragraph):
    num=1
    paragraph = paragraph.replace(".", "").replace(",", "") #replace는 할당을 해야 쓸수 있음
    list = paragraph.lower().split(" ")
    for i in list:
        print(f"{num}. {i}")
        num+=1

def List(paragraph):
    sentence = paragraph.split(". ")
    num = 1
    for i in sentence:
        if i[-1] == ".":
            i = f"{num}. {i}" 
        else:
            i = f"{num}. {i}."
        sentence[num-1] = i
        num+=1
    text = "\n".join(sentence)
    print(text)

data = Read(data)
Word(data)
List(data)
