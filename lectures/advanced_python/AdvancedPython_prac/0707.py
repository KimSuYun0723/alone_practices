print("========================실습1==========================")

f = open("write1.txt", "w")

f3 = open("Personal_info.txt", "r")
info = f3.read()

info1 = info.replace("\n\n", "\n")
name = info1.split("\n")

List = "".join(name[0::5])
List = List.split("Name: ")
ResultL = List[1::]
result = "\n".join(ResultL)
f.write(result)

f3.close()
f.close()

print("========================실습2==========================")

f2 = open("write2.txt", "w")

a = [1,2,3,4,5]
b = []
for i in a:
    b.append(str(i))
data = "\n".join(b)
f2.write(data)


f2.close()


print("========================실습3==========================")

def list_add(l,e): #프린트, 리턴 다 없는 함수도 쓸순 잇음
    l.append(e) #원본 훼손하는 함수수

a = [1,2,3]

A = list_add(a,4)

print(a) #수정되어있음
print(A) #None

"""
return은 무조건 맨 마지막
return
print
==> print 실행 X
"""

print("========================실습_함수4개=========================")
def Sum():
    a1 = input("첫번째 수를 입력 : ") #int로 바꿔야됨 근데....출력할 때 안바꾸면 감점? 출력할 때 바꾸니까 뭐..
    a2 = input("두번째 수를 입력 : ")
    result = a1+a2
    return result

def minus():
    a1 = input("첫번째 수를 입력 : ")
    a2 = input("두번째 수를 입력 : ")
    result = a1-a2
    return result

def gop():
    a1 = input("첫번째 수를 입력 : ")
    a2 = input("두번째 수를 입력 : ")
    result = a1*a2
    return result

def divide():
    a1 = input("첫번째 수를 입력 : ")
    a2 = input("두번째 수를 입력 : ")
    result = a1/a2
    return result
    
def one_1(a1,a2):
    hap = a1+a2
    minus = a1-a2
    gop = a1*a2
    divide = a1/a2
    result = f"""합: {hap}\n차: {minus}\n곱: {gop}\n나누기: {divide}"""
    return result
    

def one_2():
    a1 = input("첫번째 수를 입력 : ")
    a2 = input("두번째 수를 입력 : ")
    hap = a1+a2
    minus = a1-a2
    gop = a1*a2
    divide = a1/a2
    result = f"""합: {hap}\n차: {minus}\n곱: {gop}\n나누기: {divide}"""
    return result