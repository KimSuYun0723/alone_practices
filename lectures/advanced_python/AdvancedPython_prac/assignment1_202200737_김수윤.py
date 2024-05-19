f2 = open("phone.txt", "w")
f = open("Personal_info.txt", "r")
info = f.read()

info1 = info.replace("\n\n", "\n")
name = info1.split("\n")

List = "".join(name[4::5])
List = List.split("Phone: ")
ResultL = List[1::]
print(ResultL)

answer = []
for i in ResultL:
    num = i.replace("010-", "").replace("-", " ")
    answer.append(num)

result = "\n".join(answer)
f2.write(result)

f.close
f2.close