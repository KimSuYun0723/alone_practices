print("==============실습===============")

a = """We're studying for the loop"""

List = a.split(" ")

num = 1
for i in List:
    print(f"{num}.{i} ")
    num+=1

print("\n==============실습2===============")
jumin_list = ['950101-1234567', '891230-2345678','800101-4567890','721010-5678901', '660101-6789012', '030202-7890123', '480101-8901234', '051231-9012345', '980101-0123456']
answer = []
for i in jumin_list:
    a = i.split("-")
    if a[1][0] == 1 or 2:
        answer.append(i)
        print(i)

print("\n==============실습2===============")
jumin_list = ['950101-1234567', '891230-2345678','800101-4567890','721010-5678901', '660101-6789012', '030202-7890123', '480101-8901234', '051231-9012345', '980101-0123456']
answer = []
for i in jumin_list:
    a = i.split("-")
    if a[1][0] in "12":
        answer.append(i)
        print(i)
    else:
        continue
print(answer)


print("\n==============실습3===============")
jumin_list = ['950101-1234567', '891230-2345678', '010101-3456789', '800101-4567890', '721010-5678901', '660101-6789012', '030202-7890123', '480101-8901234', '051231-9012345', '980101-0123456']

answer = []

for i in jumin_list:
    a = i.split("-")
    if int(a[0][0:2]) <=23:
        if a[1][0] in "1234":
            answer.append(i)
            print(i)
        else:
            pass
    elif int(a[0][0:2]) >23:
        if a[1][0] in "12":
            answer.append(i)
            print(i)
        else:
            pass

    else:
        pass
    
print(answer)


