print("==========2번문제==========")
import re
f = open("quaint_vil.txt", "r")
data = f.read()

#문장 나누기
p = re.compile(r"\.|\?|\!")
new_d = ""
for d in data:
    if p.search(d):
        new_d += d + "\n"
    else:
        new_d +=d
sen = new_d.split("\n ")
sen[-1] = sen[-1].strip()
num=1
for i in sen:
    print(f"{num}. {i}")
    num+=1
f.close()

















