#assignment 5 참고_ plural -> singular
#shift+tap -> indentation 제거

dict = {'sheep': 0, 'book': 1, 'box': 2, 'city': 3, 'wife': 4, 'leaf': 5}
#sheep, books, boxes, cities, wives, leaves

while True:
    word0 = str(input("단어를 입력하세요: "))
    word = word0.lower() #복수형 단어 입력

    if word0 =="stop": #종료
        break

    for i in dict: 

        ## 딕셔너리 key 복수형 만들기
        if dict[i] ==0: 
            plural = i
        elif dict[i] ==1: 
            plural = i +"s"
        elif dict[i] ==2:
            plural = i +"es"
        elif dict[i] ==3:
            plural = i.replace(i[-1], "ies")
        elif dict[i] ==4:
            plural = i.replace(i[-2:], "ves")
        elif dict[i] ==5:
            plural = i.replace(i[-1], "ves")

        #만든 복수형이랑 입력받은 단어랑 똑같으면
        if plural == word:
            print(i) #단수형을 프린트(딕셔너리 key)
            break
        else: 
            print("Write Again!") #그게 아니라면 다시.
            continue
