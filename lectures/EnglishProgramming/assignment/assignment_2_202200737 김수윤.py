import string
alice = """Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes."""


#문자열 길이 구하기
length = len(alice)
print(f"The number of letters of the data is {length}.")
print("\n")


#소문자로 바꾸기_1(lower 활용)
low_1 = alice.lower()
print(low_1)
print("\n")


"""
#소문자로 바꾸기_2(과제와 관계없이 도전한 방법)
low_2 = alice.replace("A","a") #큰 따옴표 안에 들어가 있는 문장 빼곤, 대문자가 A와 S밖에 없음.
low_2 = low_2.replace("S","s")
low_2 = low_2.split('\"') #그래서 "" 기준으로 split해주고(대신 원본데이터 보존하는 방향으로)
low_2[1] = low_2[1].lower()
low_2[3] = low_2[3].lower() # 순서 맞춰서 소문자로 바꿔주고
low_2 = print(''.join(low_2)) #다시 합쳐줌. 하지만 문제는 큰따옴표를 다시 붙일수가 없다는점^^;;;;
print("\n")
"""


#대문자로 바꾸기
up =  alice.upper()
print(up)
print("\n")


#문장 부호 삭제하기_1(노가다?)
nadomola = alice #원본데이터 보존
nadomola = nadomola.replace(",","") #다행히 alice 데이터에는 ,". 밖에 없음.
nadomola = nadomola.replace(".","")
nadomola = nadomola.replace("\"","")
print(nadomola)
print("\n")


#문장 부호 삭제하기_2(split 활용하기)
nadomola1 = alice #원본데이터 보존
nadomola1 = nadomola1.split("\"") #문장부호를 기준으로 split을 써주면 사라지니까.
nadomola1 = "".join(nadomola1) #다시 합쳐주기
nadomola1 = nadomola1.split(".") #위 과정 반복
nadomola1 = "".join(nadomola1)
nadomola1 = nadomola1.split(",")
nadomola1 = print("".join(nadomola1))
print("\n")


#문장 부호 삭제하기_3(참고: 구글링)
#import string(line 1)
nadomola2 = alice #원본데이터 보존
for i in string.punctuation: #type(string.puctuation) 확인해보니 string.
    nadomola2 = nadomola2.replace(i, "")
print(nadomola2)
print("\n")


#"the"를 "THE"로 바꾸기
change = alice.replace("the", "THE") 
print(change)
print("\n")


#띄어쓰기로 분할하기
slice = alice.split(" ")
print(slice)
print("\n")