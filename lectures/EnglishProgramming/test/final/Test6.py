w_dic = {'sheep': 0, 'book': 1, 'box': 2, 'city': 3, 'wife': 4, 'leaf': 5}
"""dic2 = {v:k for k,v in w_dic.items()}
print (dic2)"""


while True:
    answer = str(input("단수형 or 복수형 or q : "))
    if answer == "단수":
        while True: 
            word = str(input("INPUT a word/OR say 'quit': "))
            word1 = str(word.lower())

            if word == "q":
                quit()

            elif word1 not in w_dic.keys():
                print("The word you entered is not found")
                continue
            
            else:
                ind = list(w_dic.keys()).index(word1)
                a = list(w_dic.keys())[ind]
                if w_dic[word1] == 0:
                    word2 = a

                elif w_dic[word1] == 1:
                    word2 = a +"s"

                elif w_dic[word1] == 2:
                    word2 = a + "es"

                elif w_dic[word1] == 3:
                    word2 = a.replace(a[-1], "ies")

                elif w_dic[word1] == 4:
                    word2 = a.replace(a[-2:], "ves")

                elif w_dic[word1] == 5:
                    word2 = a.replace(a[-1], "ves")

                print(f"Singular: {word1}")
                print(f"Plural: {word2}")
    
    elif answer == "복수":
        while True:
            word0 = str(input("단어를 입력하세요: "))
            word = word0.lower() #복수형 단어 입력

            if word0 =="q": #종료
                quit()

            for i in w_dic: 
                ## 딕셔너리 key 복수형 만들기
                if w_dic[i] ==0: 
                    plural = i
                elif w_dic[i] ==1: 
                    plural = i +"s"
                elif w_dic[i] ==2:
                    plural = i +"es"
                elif w_dic[i] ==3:
                    plural = i.replace(i[-1], "ies")
                elif w_dic[i] ==4:
                    plural = i.replace(i[-2:], "ves")
                elif w_dic[i] ==5:
                    plural = i.replace(i[-1], "ves")

                #만든 복수형이랑 입력받은 단어랑 똑같으면
                if plural == word:
                    print(i) #단수형을 프린트(딕셔너리 key)
                    break
                else: 
                    continue
    else:
        print("The word you entered is not found")