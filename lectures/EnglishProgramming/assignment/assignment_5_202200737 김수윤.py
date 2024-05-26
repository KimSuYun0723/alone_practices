#sheep, book, box, city, wife, leaf

# 그렇다면 복수형을 단수형으로 바꾸는 것은 어떻게 ??? 로직을 미리 짜보자.
# 형용사의 경우에는  살다/죽다(scale이 없는 경우), ~~scale에 따라서 er/more
# 동사의 경우에는..(너무 복잡해)_ 동사 1-2개만 낼 것임(자주쓰는건 거의다 불규칙이라 하더라도!), 
# 동사는 불규칙이라 할지라도 drink-> drank/sing->sang 처럼 불규칙끼리 비슷한 경우가 있어
# 안변하는 인칭대명사를 찾아라.
# take를 찾아라 -> took, taken 도 찾아야 돼... taking도 찾아야 되고... 이걸 어떻게 해야할까? -> 근데 take는 불규칙이니까 규칙변화로 생각해봐
# 규칙도 근데 d를 붙이는 것도 있고 ed를 붙이는 애도있고. 그것도 생각 으아아아아아아아악

#동사는 규칙만 낼거긴 한데 너무 잘하면 불규칙 ㅋ 1-2개만 줘서, 표를 안봐도 어떻게 변하는지 아니까 그 단어의 변화형을 알고 있으니까 eat도 ate도 eaten eats도 찾을 수 있게 만드는 것..

dict = {'sheep': 0, 'book': 1, 'box': 2, 'city': 3, 'wife': 4, 'leaf': 5}

while True:
    word = str(input("INPUT a word/OR say 'quit': "))
    word1 = str(word.lower())

    if word == "quit":
        print("QUIT!")
        break

    elif word1 not in dict.keys():
        print("Try Again!")
    
    else:
        if dict[word1] == 0:
            word1 = word1

        elif dict[word1] == 1:
            word1 = word1 +"s"

        elif dict[word1] == 2:
            word1 = word1 + "es"

        elif dict[word1] == 3:
            word1 = word1.replace(word1[-1], "ies")

        elif dict[word1] == 4:
            word1 = word1.replace(word1[-2:], "ves")

        elif dict[word1] == 5:
            word1 = word1.replace(word1[-1], "ves")

        print(word1)