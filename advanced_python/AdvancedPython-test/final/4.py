f = open("animals.txt", "r")
text = f.read()

words = text.split(" ")
dict_lenword = {}
for i in words:
    dict_lenword[i] = len(i)

answer = sorted(dict_lenword.items(), key=lambda x: x[1])

for i in range(len(answer)):
    print("%d. %s" %(i+1, answer[i][0]))

f.close()

