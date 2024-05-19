f2 = open("ani_list.txt", "w")

f = open("animals.txt", "r")
text = f.read()

words = text.split(" ")
List = []
List.append("#### 3번문제결과 202200737 김수윤 ####")
for i in range(len(words)):
    List.append("%d. %s" %(i+1, words[i]))

answer = "\n".join(List)
f2.write(answer)

f.close()
f2.close()

