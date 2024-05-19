#문장 나누고, sen_list.txt, "문장 번호, 문장 " 
f = open("sen_list.txt", "w")
f2 = open("punc_marks.txt", "r")
data = f2.read()
data = data.replace(". ", ".@").replace("\n", "@").replace("!\n", "!@").replace(".\n", ".@").replace("! ", "!@")
data = data.replace("...@", "... ").replace("@@", "@")

sentence = data.split("@")
num = 1
for i in sentence:
    i = f"{num}. {i}"
    sentence[num-1] = i
    num+=1

List = []
text = "\n".join(sentence)

first = "#2번문제# 202200737 김수윤"

List.append(first)
List.append(text)

Text = "\n".join(List)
f.write(Text)

f2.close()
f.close()