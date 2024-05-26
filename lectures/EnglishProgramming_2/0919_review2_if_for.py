#set활용해서 단어 목록 만들기
data = """She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes."""
answer = sorted(list(set(data.replace(".","").lower().split(" "))))
for i in range(len(answer)):
    print(f"{i+1}. {answer[i]}")

#len(list)를 비교해서 몇개의 단어가 지워졌는지 확인도 가능

#딕셔너리 정렬 복습하기_key, value 기준 정렬, 오름 차순 정렬 등등 상황 생각해가면서

#단어 난이도 판정 프로그램
word = str(input("단어를 입력하세요: "))
if len(word) <= 5:
    print("Your level is [beginner]!")
elif len(word) <=8:
    print("Your level is [intermediate]!")
elif len(word) >=9:
    print("Your level is [advanced]!")

#format 실습_review(2)_15
inch = 2.54
per_inch = float(input("센티미터로 변환하고 싶은 인치를 입력: "))
inch * per_inch