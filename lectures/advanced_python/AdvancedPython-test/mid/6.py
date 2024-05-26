print("==========6번 문제==========")
data = """Once upon a time, there was a young man named Jack who lived in a small village. He was a curious and adventurous person who loved exploring the world around him. One day, he decided to set out on a journey to find the legendary treasure that was said to be hidden in the nearby mountains.

As he made his way up the mountain, he encountered many obstacles and challenges. He had to climb steep cliffs, cross raging rivers, and navigate through dense forests. But he never gave up, and he kept pushing himself to reach his goal.

On the third day of his journey, he came across an old man who was sitting by the side of the road. The man had a long white beard and was dressed in tattered robes. "He who seeks the treasure must first answer my riddle.", he looked up as Jack approached and said."""

data1 = data.replace(",", "").replace(".", "").replace("\"", "").replace("\n\n", " ").lower()
data1 = data1.split(" ")

word = input("단어를 입력하세요 \n:")

c = data1.count(str(word))

if word in data1:
    print(word, ":", c)
else: 
    print("찾으시는 단어가 없습니다")