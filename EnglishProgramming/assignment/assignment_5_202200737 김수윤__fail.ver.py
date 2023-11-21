#영어 명사 활용형 만들기
# 아래 단어를 딕셔너리, if, input, infection code를 활용해서 복수형을 만들고 출력
    #sheep, book, box, city, wife, leaf
#value에 활용형이 들어가고 Key에는 NN??
#딕셔너리에 예시 단어 6개 넣고 만들면 됩니다. 
#단, 코드 자체는 나중에 딕셔너리를 확장해서 다른 단어가 들어와도 처리될 수 있게 만들어야 합니다!  

"""
NN NNS Example
0 - /- # 불규칙
1 s/book
2 es/box, pass
3 y->ies/city, cry  #근데 y 앞에 모음 오면 -s만 
4 fe-> ves/wife, knife
5 f-> ves/leaf,shelf 
9 irregular/children
"""
#sheep, book, box, city, wife, leaf

dict = {} #key에 단어, value에 NN
SameList = ["sheep", "deer", "fish", "species", "scissors", "shorts", "pants", "trousers", "jeans", "livestock", "news", "slang", "bravery", "love", "money"]

while True:
    word0 = str(input("단어를 입력하세요: "))
    word = word0.lower()
    
    #중복단어 제거

    if word == "종료":
        break

    #NN 0번
    if word in SameList:
        word1 = word
        dict[word1] = 0

    #y(-->ies), 모음+ y(--=> +-s)
    elif word[-1] == "y":
        if word[-2] in "aeiou":
            word1 = word + "s"
            dict[word1] = 1
        else: 
            word1 = word.replace(word[-1], "ies")
            dict[word1] = 3
    
    #-e(--> +-s), -fe(-->-ves), 
    elif word[-1] == "e":
        if word[-2] =="f":
            word1 = word.replace(word[-2:], "ves")
            dict[word1] = 4
        else:
            word1 = word + "s"
            dict[word1] = 0

    #-f(-->ves)
    elif word[-1] == "f":
        word1 = word.replace(word[-1], "ves")
        dict[word1] = 4

    #-s,-x,-z,-sh,-ch(-es)
    elif (word[-1] in ["s","x","z"]) or (word[-2:] in ["sh","ch"]):
        word1 = word + "es"
        dict[word1] = 2

    #-o, -e,-th,-ph
    elif (word[-1] in ["o","e"]) or (word[-2:] in ["th","ph"]):
        word1 = word + "s"
        dict[word1] = 1

    else:
        word1 = word + "s"
        dict[word1] = 1

    print(word1)

print(dict)

keys = list(dict.keys())
print(keys)

"""
#giraffes, roofs
"""