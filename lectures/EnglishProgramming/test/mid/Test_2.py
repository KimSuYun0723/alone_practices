sophie = """Following someone's advice, Sophie went back to the park and searched the area, looking for any clues. Suddenly, she saw something glimmering in the bushes. She ran towards it and found a small, hidden treasure chest. Sophie carefully opened the chest and inside, she found more coins and a note. The note read:
'Congratulations! You have found my treasure. Please keep one coin for yourself and share the rest with your friends and family. Remember to always follow your curiosity and keep exploring.'
Sophie was overjoyed. She took one coin and shared the rest with her loved ones. From that day on, she always carried the coin with her as a reminder to follow her curiosity and explore the world around her.
Her adventure taught her an important lesson about being curious, asking questions, and investigating. Therefore, it really made her feel a lot.
"""

#문장부호 삭제 후 전체를 하나의 문자열로 담아 출력
#apostrophe 는 삭제하지 말고 한칸 공백을 삽입(cat's >cat 's)
print("========== MAKE STRING ==========")
sophie1 = sophie
sophie_1 = sophie.replace("!", "").replace(",", "").replace(".", "").replace(":", "").replace("\n\'","").replace("\'\n","").replace("\'", " \'")
#/n' 을 "" 가 아니라 /n으로 바꿔야지 미친놈아... 제발...
#' 다음에 s가 있는지 확인하면 지울 수 있음(물론 항상은 아니지만, 이 데이터에서는 그 정도를 원했음)
#s를 찾아서 처리한다면=> 's를 먼저 처리하고, 그다음에 single quote를 지우는 방식
print(sophie_1, "\n")

"""
의미를 볼때 문장 부호는 잘 지우지 않음
단어를 볼때나 문장 부호를 주로 지움
"""



