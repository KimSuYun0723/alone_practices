num = [69, 44, 5, 43, 31, 81, 15, 46, 84, 99, 53, 29, 94, 43, 39, 21, 58, 28, 50]

List = []
k = 0
for i in num:
    if (i>=30) and (i<=40):
        if k<=15:
            List.append(i)
    k+=1
print(List)