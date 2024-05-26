sophie_2 = """Sophie went back to the park and searched the area, looking for any clues. Suddenly, she saw something glimmering in the bushes. She ran towards it and found a small, hidden treasure chest. Sophie carefully opened the chest and inside, she found more coins and a note. The note read:
'Congratulations! You have found my treasure. Please keep one coin for yourself and share the rest with your friends and family. Remember to always follow your curiosity and keep exploring.'
Sophie was overjoyed. She took one coin and shared the rest with her loved ones. From that day on, she always carried the coin with her as a reminder to follow her curiosity and explore the world around her.
Her adventure taught her an important lesson about being curious, asking questions, and investigating. Therefore, it really made her feel a lot.
"""

sophie2 = sophie_2

#1. "her" 개수 구하고 "The frequency of the word her is 00."
print("========== 1. ==========")
sophie01 = sophie2.lower()
num = sophie01.count("her")
print("The frequency of the word her is", num, ".") #comma가 아니라 + 연산자로 뽑았어야하고, +연산자를 썼으면 전부 string으로 바꿔서 넣었어야 해
#단어 her를 세라고 했는데 왜 String Sequence HER를 세고 ㅈㄹ이니 진짜 정신 안차리니^^
    #Sting 말고 List에서 셌어야지 ㅠㅠ
#counter example이 있다고 생각하고 문제에 들어가야지...


#2. 전체 단어 개수 구하고 "The number of words in the text is 00."
print("\n\n========== 2. ==========")
#count의 대상 자체를 String으로 할지, List로 할지 생각을 해야지 ㅜㅜ
sophie02 = sophie2
sophie02 = sophie02.replace("!", "").replace(",", "").replace(".", "").replace(":", "").replace("\n\'","").replace("\'\n","").replace("\n"," ")
sophie02_answer = sophie02.split(" ")
total_num = len(sophie02_answer)
print("The number of words in the text is", total_num, ".")


#3. 공백 포함 문자수와 공백 제외 문자수를 구하는 프로그램 작성, 
# "The number of characters including spaces is 000."
# "The number of characters excluding spaces is 000."
print("\n\n========== 3. ==========")
sophie03 = sophie02
sophie03_2 = sophie03.split(" ")
len_in = 2*len(sophie03_2)-1
len_ex = len(sophie03_2)
print("The number of characters including spaces is", len_in, ".")
print("The number of characters excluding spaces is", len_ex, ".")
#공백 포함 문자수도 있고 공백 제외 문자수도 있잖아. 공백 포함 글자수/단어수 -> 공백, 문장부호 포함해서 세는 것임..
#뉴 라인도 빼야 공백 제외임.


#4. while 반복문과 remove 함수 활용해서 "she" 모두 삭제 하고 출력하세요(자료형 무관)
print("\n\n========== 4. ==========")
sophie04 = sophie02
sophie04 = sophie04.lower()
sophie04_list = sophie04.split(" ")
print(sophie04_list)
# word2 = word[:] 이렇게 카피 해야지, 그냥 word를 넣으면 똑같이 움직인다고;;;
#remove는 list로
#replace를 쓰고 싶었으면 string인건데, she 지울 때 brushes 에서 she가 지워졌을 테니까, "단어"상태에서 replace를 썼어야 하는 것임.


i =0
while ("she" not in sophie04): #반복을 몇번 할 것이냐? 가 .. 포인트였음. 검토할때 word 이용해서 she를 찾고 비교해봐도 괜찮음.
    break
else:
    print(sophie04_list.index("she"))
    sophie04_list.remove("she")
    i += 1
    print(i)
print(sophie04_list)


#5. 단어와 단어 빈도 구하여 dict 자료형에 담은 후 빈도를 기준으로 내림차순 정렬하여 출력
    # 딕셔너리 key value를 뽑아서, 콜론 붙이고 띄어쓰기 할 수 있는지.
    #그냥 딕셔너리만 출력했으면 안되는 것임.
    #빈도만 내림차순으로 잘 출력되게.
print("\n\n========== 5. ==========")
dict = {}
sophie05 = sophie02.lower()


