#call,close,copy,pay,enjoy,stop,jog
#얘는 딕셔너리로 하는게 아님. 하면 좋겠지만 너무 다양하니까<== text를 주겠다
#text initializing -> 단어들만 split해서 list로. -> text 하나씩 참조하면서, 활용형
"""
리스트 요소 하나씩 참조
만약 count_word[0][0]이랑 첫글자가 똑같으면,
    그 단어랑 활용형 4개랑 똑같은지 확인.
    똑같으면 숫자 하나 추가.
"""
f = open("austen-emma.txt", "r")
text = f.read()

#initializing
text = text.lower().replace(".", "").replace(",", "").replace("--", " ").replace("_", "").replace("'s", "").replace("\n", "").replace(";", " ")
words = text.split("  ")
words = " ".join(words).split(" ")
count_word = ["live", "wish"]
num = 0
c = 0

#사실 count_word를 활용안하긴 했음.
for i in words:
    if count_word[0][0] == i[0]:
        if count_word[0] == i:
            num+=1
        elif count_word[0]+"s"== i:
            num+=1
        elif count_word[0]+'d'== i:
            num+=1
        elif count_word[0][:-1]+"ing"== i:
            num+=1
        print(i, num)
print("final", num)


f.close
        

