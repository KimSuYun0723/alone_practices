f2 = open("sen_list.txt", "w")
f = open("emily.txt", "r")
data = f.read()

#.replace(". ", "\n").replace(".", "")

#문장 나누기 
sentence = data.split(". ")
num = 1
for i in sentence:
    i = f"{num}. {i}" #. 추가
    sentence[num-1] = i
    num+=1

text = "\n".join(sentence)
f2.write(text)

f.close()
f2.close()


#strip 배우기_lstrtp, rstrip 왼쪽 오른쪽
"""
a.lstrip() : 왼쪽에 있는 공백을 지워주는 것임. ???
"""