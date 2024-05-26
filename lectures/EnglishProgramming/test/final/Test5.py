w_dic = {'sheep': 0, 'book': 1, 'box': 2, 'city': 3, 'wife': 4, 'leaf': 5}
"""dic2 = {v:k for k,v in w_dic.items()}
print (dic2)"""

while True:
    word = str(input("INPUT a word/OR say 'quit': "))
    word1 = str(word.lower())

    if word == "q":
        break

    elif word1 not in w_dic.keys():
        print("Try Again!")
    
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