"""
f = open("C:\\Users\\jenny\\Downloads\\emily.txt", "r")
emily = f.read()
list = []
emily = emily.replace(".", "").replace(",", "")
emilyL = emily.split(" ")
for i in range(len(emilyL)):
    if emilyL[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  #IndexError
        print(emilyL[i])
        list.append(emilyL[i])

f2 = open("emily_w.txt", "w")
for i in range(len(list)): #for loop 돌려서 넣을거면... +\n이나 " " 같이 구분자를 따로 넣어줘야함..
    f.write(list[i])

f.close()
f2.close()
"""
list = []
with open("C:\\Users\\jenny\\Downloads\\emily.txt", "r") as f:
    emily = f.read()
    emilyL = emily.split(" ")
    for i in range(len(emilyL)):
        if emilyL[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            list.append(emily[i])

    with open("emily_2.txt", "w") as f2:
        up = "\n".join(list)
        f2.write(up)

