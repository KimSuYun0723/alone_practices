Data = "A machine-readable lexical database organized by MIT Technology Review in 2000"
only_upper = []
upper_n_lower = []
include_else = []
only_num = []
l = Data.split(" ")

#if elif else 문이면 1개만 걸려서 안됨
for i in l:
    if i.isupper() == True: #대문자
        only_upper.append(i)
    if (i.islower() == False) and (i.isupper() == False): #대소문자
        if (i.isalnum() == True) and (i.isdigit() == False):
            upper_n_lower.append(i)
    if i.isalnum() == False: #기호 포함
        include_else.append(i) 
    if i.isdigit() == True: #숫자
        only_num.append(i)

print("대문자만 : ", only_upper)
print("대+소문자 : ", upper_n_lower)
print("기호포함 : ", include_else)
print("숫자만 : ", only_num)

"""
for i in l:
    print(i)
    print("is digit: ", i.isdigit())
    print("is alphat: ", i.isalpha())
    print("is alnum: ", i.isalnum())
    print("is lower: ", i.islower())
    print("is upper: ", i.isupper())
    print("is space: ", i.isspace())
"""

#8p
f = open("C://Users//jenny//Downloads//TheNorthWind&theSun.txt", "r")
data = f.read()
data0 = data.splitlines()
for i in data0:
    print(i)
    print()
f.close()

#9p
a = input().split()
l = list(map(int, a))
print(l)

#마지막 직전
f = open("TEST.txt", "w")

data = "111파이썬111"

f.write(data.center(10))
f.write(data.ljust(10))
f.write(data.zfill(10))
f.close()

#마지막 실습
data = "Good morning, Mr. Smith. How are you? I'm fine, thank you. How's the weather outside? It’s rainy today."
#미스터는 버리고 할 것임_처리 고민해보기
d = data.replace(".", "\n").replace("?", "\n")
sen = d.splitlines()

for s in sen:
    print(s.lstrip())

import re
p = re.compile("like.*")
string = ["like", "likely", "likelihood"]

for s in string:
    m = p.search(s)
    #m은 매치된 단어만 알려주는게 아니라 다양한 정보를 다알려주는 아이임.
    if m:
        print(s, "YES")
    else:
        print(s, "NO")
        
p = re.compile("ca+t")
string = ["cat", "caat", "caaaaat"]

p = re.compile("[A-Z]+")
string = ["CAT", "Caat", "caaaaat"]

p = re.compile("ca{2}t")
string = ["CAT", "caat", "caaaaat"]

p = re.compile("ab?c")
string = ["abc", "ac"]

p = re.compile("a|b")
string = ["abcd", "ac"]

for s in string:
    m = p.search(s)
    #m은 매치된 단어만 알려주는게 아니라 다양한 정보를 다알려주는 아이임.
    if m:
        print(s, "YES")
    else:
        print(s, "NO")