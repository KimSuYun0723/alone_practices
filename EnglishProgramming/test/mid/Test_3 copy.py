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
print("The frequency of the word her is", num, ".")


#2. 전체 단어 개수 구하고 "The number of words in the text is 00."
print("\n\n========== 2. ==========")
sophie02 = sophie2
sophie02 = sophie02.replace("!", "").replace(",", "").replace(".", "").replace(":", "").replace("\n\'","").replace("\'\n","").replace("\n"," ")
sophie02_answer = sophie02.split(" ")
print("틀리지말자 : ", sophie02_answer)
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



#4. while 반복문과 remove 함수 활용해서 "she" 모두 삭제 하고 출력하세요(자료형 무관)
print("\n\n========== 4. ==========")
sophie04 = sophie02
sophie04 = sophie04.lower()
sophie04_list = sophie04.split(" ")
print(sophie04_list)

while ("she" not in sophie04):
    print(sophie04_list.index("she"))
    sophie04_list.remove("she")

print(sophie04_list)


#5. 단어와 단어 빈도 구하여 dict 자료형에 담은 후 빈도를 기준으로 내림차순 정렬하여 출력
print("\n\n========== 5. ==========")
dict = {}
sophie05 = sophie02.lower()


