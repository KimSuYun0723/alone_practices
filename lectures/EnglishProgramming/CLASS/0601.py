def do_nothing():
    pass

do_nothing()
##########################################
def lets_print():
    print("함수를 만들고 테스트 해보자!")

lets_print()
################################################
def agree():
    return True

a  = agree()
print(a)

if a:
    print("동의")
else:
    print("반대")
#############################
#프린트가 없는 함수는 print를 써야만! 출력값이 있음, 근데 return이랑 print 둘다 있는 것도 있음

####################

def Rfile(file):
    f = open(file, "r")
    data = f.read()
    return data

a = Rfile("emily.txt") #이것까지 해야돼. 호출!!
print(a)

"""def save(data, result):
    data.write(result)
    f.close() ###
    return data"""


###########################################
def open_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

def word(cont):
    w = cont.split()
    print(w)
    return w

def write_file(cont, file):
    f1 = open(file, "w")
    f1.write(cont)
    f1.close() ##return, print 원래는 다 필요 없는 함수임.
    #return cont 
    # #그냥 찜찜하니까 이렇게해도 상관은 없지만

a = open_file("emily.txt")
b = write_file(a, "text.txt") # 출력되는게아무것도 없어야 정상이긴함. 
print(b) #불안하니까 출력

a = open_file("emily.txt")
w = word(a)
write_file(w, "text.txt") #애초에 return을 스트링으로 받거나, 아니면 write_file을 호출하고 if문 활용해서 만약 리스트니? 리스트면, for loop을 돌린달지..

"""
1.복수주고 단수 찾는...딕셔너리 정해져있음
2.open-opend-opening 이런 인플렉션이 있는 동사들.. 불규칙은 안할 것임.
오픈을 담은 변수로 찾는달지, +ed를 찾아야지
open자리에 다른 단어를 넣으면 찾을 수 있도록

함수도 고민해보고 알려드릴게요_기말고사"""

##############################
def greeting():
    print("안녕하세요")

def greeting2():
    return "안녕하세요" #입력값없어도 걍 안녕하세요가 나옴

greeting()
print(greeting2())

def kiosk(lan):
    while True:
        if lan=="한국어":
            print("안녕하세요")
            break
        elif lan =="English":
            print("Hello")
            break
        else:
            print("다시 입력해보세요")

lang = str(input("한국어 or English 중에 한가지를 입력하세요: "))
kiosk(lang) #이런식으로 호출

