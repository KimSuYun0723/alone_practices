emily = """Once upon a time, there was a little girl named Emily. She lived in a small town with her parents and her beloved white dog, White. Emily loved playing outside and exploring the nearby woods with White by her side."""


#1. 고유명사를 제외한 나머지 문자열만 소문자로 바꾸는 프로그램 작성
print("========== 1. ==========") #while을 2번 쓰면 조건문처럼 풀 수 있는 문제
emily1 = emily
proper =["Emily", "White"]
emily01 = emily1.split("White")
emily01[0] = emily01[0].lower()
emily01[1] = emily01[1].lower()
emily01[2] = emily01[2].lower()
Emily = "White".join(emily01)
EMILY = Emily.replace("emily", "Emily")
print(EMILY)



#2. 단어 목록을 오름차순 정렬 -> 슬라이싱으로 홀수 인덱스에 있는 단어만 출력
print("\n\n========== 2. ==========")
emily2 = emily
emily2 = emily2.replace(".", "").replace(",", "")
emily2 = emily2.lower()
emily2 = emily2.split(" ")
emily2 = list(set(emily2))
arrange = sorted(emily2)
print(arrange[::2]) #홀수 인덱스(1부터 시작) != 홀수(1부터 시작이니까 인덱싱은0번부터)


#3. 데이터를 띄어쓰기 단위로 리스트 -> input으로 인덱스 번호를 입력받고 해당 인덱스 값을 "#####"
#전체 리스트 출력
print("\n\n========== 3. ==========")
emily3 = emily
emily_list = emily3.split(" ")
index = int(input("인덱스 번호 입력 : "))
emily_list[index] = "#####"
print(emily_list)