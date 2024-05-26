#!/usr/bin/env python3

print("---3번 문제---")

data = """Once upon a time, there was a young man named Jack who lived in a small village. He was a curious and adventurous person who loved exploring the world around him. One day, he decided to set out on a journey to find the legendary treasure that was said to be hidden in the nearby mountains.


As he made his way up the mountain, he encountered many obstacles and challenges. He had to climb steep cliffs, cross raging rivers, and navigate through dense forests. But he never gave up, and he kept pushing himself to reach his goal.


On the third day of his journey, he came across an old man who was sitting by the side of the road. The man had a long white beard and was dressed in tattered robes. "He who seeks the treasure must first answer my riddle.", he looked up as Jack approached and said."""

print("---3-1번 문제---")

print(f"공백 포함 글자수는 {len(data)}입니다.")
r_space = data.replace(" ", "").replace("\n", "")
print(f"공백 제외 글자수는 {len(r_space)}입니다.")

print("---3-2번 문제---")

paragraph = data.split("\n\n\n")
print(f"단락 개수: {len(paragraph)}개")

print("---3-3번 문제---")

data_he = data.replace(" he ", " #### THE MAN #### ", 2)
data_he = data_he.replace(" #### THE MAN #### ", " he ", 1)
print(data_he)

print("---3-4번 문제---")

data_words = data.lower().replace(",", "").replace(".", "").replace('"', "").split()
unique_words = list(set(data_words))
words_sorted = sorted(unique_words)

i = 0
while i < len(words_sorted):
	print(f"{i + 1}. {words_sorted[i]}")
	i += 1