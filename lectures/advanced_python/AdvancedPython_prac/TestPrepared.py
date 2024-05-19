#글자수 구하기/단어replace/unique단어리스트
text = """Once upon a time, there was a young man named Jack who lived in a small village. He was a 
curious and adventurous person who loved exploring the world around him. One day, he 
decided to set out on a journey to find the legendary treasure that was said to be hidden in 
the nearby mountains.
As he made his way up the mountain, he encountered many obstacles and challenges. He 
had to climb steep cliffs, cross raging rivers, and navigate through dense forests. But he never 
gave up, and he kept pushing himself to reach his goal.
On the third day of his journey, he came across an old man who was sitting by the side of 
the road. The man had a long white beard and was dressed in tattered robes. "He who seeks 
the treasure must first answer my riddle.", he looked up as Jack approached and said."""

#원본 유지
data = text[0:-1]+text[-1]

#글자수
print("====================글자수=======================")
print(len(data))

#initializing(문장부호 제거)
data_clean = data.replace(".", "").replace(",", "").replace("\"", "").replace("\n", " ").replace("  ", " ")
print("\n====================문장부호 제거=======================")
print(data_clean)

#소문자
print("\n====================소문자=======================")
data_low = data_clean.lower()
print(data_low)

#unique 단어 리스트
print("\n====================unique 단어 리스트=======================")
print("\n".join(sorted(list(set(data_low.split(" "))))))


info = """Name: Kim Minju
Age: 22
Student_id: 20211020
Location: Seoul, South Korea
Phone: 010-1234-5678

Name: Lee Jihyun
Age: 20
Student_id: 20222021
Location: Busan, South Korea
Phone: 010-9876-5432

Name: Park Hyunwoo
Age: 25
Student_id: 20201022
Location: Incheon, South Korea
Phone: 010-5555-5555

Name: Choi Soomin
Age: 21
Student_id: 20221023
Location: Gwangju, South Korea
Phone: 010-1111-2222

Name: Kang Jaewon
Age: 23
Student_id: 20211024
Location: Daegu, South Korea
Phone: 010-9999-8888"""

#데이터에서 이름만 출력
info1 = info.replace("\n\n", "\n")
name = info1.split("\n")
print(name[0::5])
List = "".join(name[0::5])
List = List.split("Name: ")
print(List[1::])


# 나이순으로 이름과 나이출력


# 특정학번인사람만 출력

