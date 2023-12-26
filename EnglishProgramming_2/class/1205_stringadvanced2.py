#정규표현식1
import re
data = "good morning, mr. smith. how are you? i'm fine, thank you. how's the weather outside? it's rainy today."

#문장 부호 모두 지우기
minus = re.compile("[.?,]")
a0 = re.sub(minus, "", data) #mr. smith 처리 주의
a1 = re.sub("mr", "mr.", a0)
print(a1)
print("data=====",data)

#prof
p = re.compile(r"\.|\?|,|'")
n_data = re.sub(p, "", data)
print(n_data)

#문장 나누기
first = re.sub("mr.", "mr", data)
minus2 = re.compile("[.?]")
split_sen0 = re.sub(minus2,"\n", first)
split_sen00 = re.sub("mr", "mr.", split_sen0)
split_sen = split_sen00.split("\n ")
print(split_sen)


#prof
p = re.compile(r"\.|\?")
#?로 나눠버리면 "소비"됨. ?가 사라지니까. 우린 필요해~
new_d = ""
for d in data:
    if p.search(d):
        new_d += " " + d + "\n"
    else:
        new_d += d
print(new_d)
sen = new_d.split("\n")

#믄징부호 앞에 공백지우기
sen1 =[]
p = re.compile(r"([\.\?])")
for s in sen:
    ss = re.sub(p, r"\1", s)
    sen1.append(ss)

#공백지우기1
re_sen = []
for s in sen:
    s = s.lstrip()
    re_sen.append(s)
print(re_sen)

    
#prof_공백지우기2
sen2 = list(map(lambda x: x.lstrip(), sen))
sen2 = list(filter(lambda x: x !="", sen2)) #내용물이 있는것만 집어 넣어줘
#공백이 아닌 것만 filter하기. map은 적용만 하고 filter는 적용하고 만족하는 것을 남김.

#문장의 첫 글자만 대문자로 바꾸기
#정규표현식 할수는 있겠지만, 여기선 슬라이싱이 더 간편해
sen3 = []
for s in sen2:
    sen3.append(s[0].upper()+s[1:])
print(sen3)

#lambda
a = lambda x : x*5
a(3)
a = lambda x,y : x+y
print(a(1,2))

#정규표현식심화2 3p
kim = "Kim 123456-1000000"
#주민번호 뒷자리
m = re.search("([a-zA-Z]) ([0-9]+)-([0-9]{7})", kim)
#1만 들어와도 주민등록번호 될 수도 있으니까, 자리수도 설정해줘야겠지
#{7}을 6으로 수정하고 앞에를 1로 설정하면 남자 여자도 뽑을 수 있겠지
print(m.group(3))
#없는걸 그룹하려고 하면 에러가난다. -> 예외처리 필요

lee = "Lee 010-1234-5678"
m1 = re.search("([a-zA-Z]) ([0-9]+)-([0-9]+)-([0-9]+)", lee)
print(m1.group(1))
print(m1.group(2))
print(m1.group(4))

#8p
data = "Good morning, Mr. Smith. How are you? I’m fine, thank you. How’s the weather outside? It’s rainy today."
re.split(r"\. |\? ", data) #모양은 예뻐졌지만 문장부호를 소비해버림
#space없어져서 괜찮은데, 마지막 문장부호가 남아있게 됨.
#물론 다시 처리해주면 되지만, 마지막이 문장부호로 끝난다는 보장이 없응께.

#10p
p = re.compile(r"\w+(?=:)") #만족해야하지만, 소비되지 않음.
# = 우리에게 주지 않음.
script = "Joey: Instead of...?"
m = p.findall(script)
print(m)
#이름을 뽑아야할때는 첫글자부터 매칭되어야 하는 match도 좋겠지
#지금은 여기가 1줄 짜리라 findall을 쓴거지만, 조심해야함.

p = re.compile(r"\w+(?=\.)") #alpha numeric에는 뭐가 없어서 
script = "good morning, mr. smith. how are you? i'm fine, thank you. how's the weather outside? it's rainy today."
m = p.findall(script)
print(m) #단어를 알아서 단어대로 뽑아주는게 아니야.

#11p
p = re.compile(r"(?<=:).+")
script = "Joey: Instead of...?"
m = p.findall(script)
print(m) 

#12p
data = """ ABC01: $23.45
HGG42: $5.31
CFMX1: $899.00
XTC99: $69.96
Total items found: 4"""

#위 데이터에서 금액만 추출하여 합계 구하기
p = re.compile(r"(?<=\$)[0-9]+\.[0-9]+")
m = p.findall(data)
print(m)
total = sum(list(map(lambda x: float(x), m)))
print(total)

#14p
d1 = """I paid 30000won for 100 apples,
50 oranges, and 60 pears.
I saved 5000won on this order."""
d2 = """I paid $30 for 100 apples,
50 oranges, and 60 pears.
I saved $5 on this order."""
p = re.compile(r"\b\d+(?!won)\b") #자꾸 3000이 나오는 이유가 뭐냐고...
#=> 워드 바운더리 쓰자
m = p.findall(d1)
print(m)

p = re.compile(r"\b(?<!$)\d+\b") #교수님은 되는데 왜 나는 안되냐;;;
m = p.findall(d2)
print(m)

#15p
data = "Good morning, Mr. Smith. How are you? I’m fine, thank you. How's the weather outside? It's rainy today."
p1 = re.compile(r"(?<=[A-Z][a-z])\.")
print(p1.findall(data))
data = re.sub(p1, "&", data)
print(data)

