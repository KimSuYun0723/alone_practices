print("==========if_실습_(1)==========") #41583
#1. 1부터 500까지 3의 배수만 더하기 -while,if 중첩
i = 0
sum = 0
while i<=500:
    #i += 1 #수윤아 뻘짓하지말자
    if (i%3 == 0):
        sum += i
    i += 1
print(sum)

#++ 종료라고 입력하기 전까지 계속 인풋을 받게 한다음, 종료 누르면 종료될 수 있도록.
print("==========if_실습_(2)-2==========")
while True:
    word = str(input("단어를 입력하세요: "))
    if word == "종료":
        break
    else: 
        if "a" in word: #이렇게 중첩반복문 안써도 그냥 if-elif-elif로 가능한데.... 왜 이렇게 했니?
            print(word, ": a")
        elif "b" in word:
            print(word, ": b")
    #만약 a도 b도 종료도 아닌, 다른게 입력이 될 경우에, "Enter another word" 라고 입력받게 else 쓸 수도 있음.
    #문장부호처리, 대소문자 처리, 등등 얼마든지 변형 가능


print("==========if_실습_(3)==========")
#3. 복수 명사라면 "단어: plural noun", 단수명사라면 "singular noun 출력"
nouns = ['dog', 'dogs', 'cat', 'cats', 'book', 'books', 'chair', 'chairs', 'table', 'tables','song', 'song']
j = 0

while j<=len(nouns[j]):
    if "s" in nouns[j]: #엥 그냥 처음부터 이거 안쓰고 nouns[j][-1] =="s"라고 할 수 있잖아
        if nouns[j][-1] == "s":
            print(nouns[j], ": plural noun")
        else:
            print(nouns[j], ": singular noun")
    else:
        print(nouns[j], ": singular noun")
    j += 1

#단수인데 s로 끝나는애들, 불규칙 복수명사는 이렇게 할 수는 없어. 마지막 글자만 보고 판단하는 것은 무리데쓰
print("========== 보여주기 ==========")
a = "Mary eats apples and pears everyday"

if "appeles" and "pears" in a:
    print("yes")

if "apples" in a and "pears" in a: #가급적이면 이렇게.. 왜냐면 위처럼 풀어서 안될 때도 있어
    print("yes")

if ("appeles" and "pears") in a: # 아니면 이렇게 묶던가
    print("yes")


#Input 단어에 “e”와 “a” 모두 X -> “case 1”
# “e”는 있고, “a”는 없는 경우 “case 2”
# “e”도 있고 “a”도 있는 경우 “case 3”
print("========== if 중첩구문 실습 ==========")
str = str(input("단어를 입력하시오: "))

## 아니 이거 if- elif- 이거 순서 보고 구성을 해야지!!!!!! case 3-2-4-1 순으로 해야함;;;;
#이런 우선순위를 생각해야함...
#1. 조건을 더욱 정교하게(안겹치게) 만들던가, 2. 아니면 타이핑을 줄이고 case 순서 바꿔서 출력하거나.
if ("e" and "a") not in str:
    print("case 1")
elif ("e" in str) and ("a" not in str):
    print("case 2")
elif ("e" and "a") in str:
    print("case 3")
elif ("a" in str) and ("e" not in str):
    print("case 4")

#("e" and "a") in str ## 이렇게 하지마.. 이렇게 해도 잘 아노대... --> 왜? 왜 안돼???

print("========== 실습 ==========")
#1. 모음으로 시작하는 단어라면 "an"
#word = str(input("단어를 입력하시오: ")) #TypeError: 'str' object is not callable 먼 개소리여

word = input("단어를 입력하시오: ")

print("========== 실습(1) ==========")
if word[0] == "a" or "e" or "i" or "o" or "u":
    print("an")


#2. 모음으로 시작하는 단어라면 "an 단어"
print("========== 실습(2) ==========")
if word[0] == "a" or "e" or "i" or "o" or "u":
    print("an",word)


#3. 모음으로 시작하고 "s"로 끝나지 않는 단어라면 "an 단어" 출력하기
print("========== 실습(3) ==========")
if word[0] == "a" or "e" or "i" or "o" or "u":
    if word[-1] != "s":
        print("an", word)
    else:
        print("ERROR")

#1,2/1/2/1,2 둘다 아닌 = 이렇게 4가지 경우의 수로 나눌 수가 있는데, 이걸 나누는 것도 사람들마다 다른 것.

if word[0] in "aeiou":
    if word[-1] != "s":
        print("PLURAL with vowel: an "+ word)
    else:
        print("NOT PLURAL(with vowel)")
else:
    if word[-1] != "s":
        print("PLURAL(no vowel)")
    else:
        print("NOT PLURAL(no vowel)")
    print("")

proper = ["Alice", "White", "Rabbit"]
word = ["Alice", "a", "girl", "of", "seven", "years"]

num1=0
num2=0
while num1<len(word):
    while word[num1]!=proper[num2]:
        print(word[num1].lower())
        