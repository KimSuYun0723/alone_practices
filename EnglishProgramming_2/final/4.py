print("==========4번문제==========")
import re
f = open("friends_1_1.txt", "r")
data = f.read()

#등장인물
p = re.compile(r"\b[A-z][a-z\s]*\b(?=:)")
p2 = re.compile(r"\b(Priest) ([a-z]+) ([A-Z]+)\b(?=:)")
m2 = p2.search(data).group()
m = p.findall(data)
excepts = ["Scene"]
l_ = sorted(list((set(m)-set(excepts))))
plus = [m2]
l = sorted(list((set(m)-set(excepts))|set(plus)))
#1번 출력
print("1번출력 =========")
for i in range(len(l)):
    print(f"{i}. {l[i]}")

#2번 출력
print("2번출력 =========")
for i in l_:
    c = m.count(i)
    print(f"{i}: {c}")

f.close()












