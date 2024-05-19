############################# pass #############################
print("========== PASS 실습 ==========")
proper = ["Alice", "White", "Rabbit"]
word = ["Alice", "a", "girl", "OF", "seven", "years"]
i = 0

while i<len(word): #왜 <인지도 함 봐봐
    if word[i] in proper:
        pass
    else:
        #print(word[i].lower())
        word[i] = word[i].lower() ### 이렇게 바꿔야 바뀌지;;;
    i+=1
print(word)

############################# % #############################
print("========== % 실습 ==========")
# 이 아이의 단점 : 실수로 d랑 f랑 s를 잘못 맞추면 오류가 남.

freq = 100
r_freq = 5.3 #실수니까 %f로 5.300000 -> 0 안나오게 할 수 있는데 애초에 %가 유행이 아니라..
word = "the"
a = "The frequency of word 'the' is %d." % freq
print(a)
b = "The ratio of word 'the' is %f." % (r_freq)
print(b)
c = "I'm looking for the word '%s'." % word
print(c)
d = "The frequency of word '%s' is %d, and the relative frequency is %f" % (word, freq, r_freq)
print(d)

"""
a = "%d" % word
print (a) #Error

근데
a = "%s" % freq
print(a) #파이썬 에서는 freq도 그냥 s로 하나봐
"""

############################# format #############################
print("========== format 실습 ==========")
#얘는 뒤에 다시 변수를 쓰는게 불편해!

per_inch = 2.54
inch = 24
cm = inch * per_inch
print ("{0}인치 = {1}센티미터".format(inch, cm))
print ("{}인치 = {}센티미터".format(inch, cm)) #순서 똑같으면 인덱스 입력 안해도됨
# or
result = "{0}인치 = {1}센티미터".format(inch, cm)
print(result)

############################# f-string #############################
print("========== f-string 실습 ==========")
name = "John"
age = 21
s = f"{name}은 {age}살 입니다."
print(s)

d = "The frequency of word ‘{word}' is {freq}, and the relative frequency is {r_freq}"
print(d)

############################# for #############################
print("========== for문 실습 ==========")

fruit = ["blueberry", "banana", "strawberry", "cranberry", "tomato", "mango"]
for i in range(5): #range(len(fruit)) 이 더 좋다~ 하드코딩 아니고 소프트 코딩~ 제발~
    print(i, fruit[i])

for i in range(len(fruit)): 
    print(i, fruit[i])
    if i ==30: # 가지고 있는게 6개 까지여도 if로 뒤에 처리해주면 오류는 안남
        break

"""
fruit = ["blueberry", "banana", "strawberry", "cranberry", "tomato", "mango"]
for i in range(7): #IndexError_리스트 요소 개수 만큼 잘 지정해야함.
    print(i, fruit[i])
"""
#꼭 i를 인덱스로 사용하지 않아도, 그냥 반복 횟수 정도로 활용해도 괜찮음

############################# range #############################
print("========== range 문 실습 ==========")
fruit = ["blueberry", "banana", "strawberry", "cranberry", "tomato", "mango"]
for i in range(0,4,2): #짝수 인덱스 != 짝수 번째
#for i in range(0, len(fruit), 2):
    print(i)
    #if i ==4:
    break #이렇게 인덱스 4가 되면 벗어나게 하는 방법도 있음

for i in range(len(fruit)):
    if i%2 ==0:
        print(fruit[i])


i_list = []
for i in range(1,11):
#for i in range(10,0,-2):
    i_list.append(1)

print(sum(i_list))


print("========== num1 ==========")
a ="We are studying for loop"
a0 = a.replace(".","").replace(",", "")
a0 = a0.lower()
a0List = a0.split(" ")

print("========== num1 ==========")
for i in a0List:
    print(i)

print("========== num2 ==========")
for i in a0List:
    k=0
    for j in i:
        if j in "aeiou":
            k+=1
    print(i+":", k, "\n")

print("========== num3 ==========")
a=0
for i in a0List:
    k=0
    for j in i:
        if j in "aeiou":
            k+=1
    a+=1
    print(f"{a}.", i+":", k, "\n")
            



#딕셔너리를 넣으면 key만 도는데, value를 출력하라고 하면
"""
for i in dic_v:
    print(i, dic_v[i])
"""
