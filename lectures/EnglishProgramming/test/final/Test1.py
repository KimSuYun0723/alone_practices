#오름차순 정렬, 단어 앞에 단어 번호도 넣으세요
f = open("walk.txt", "r")
data = f.read()

num=0 #while문 실행 횟수를 제어할 변수

#문장 부호 제거
data = data.replace(".", " ").replace("\n", " ").replace(",", " ").replace("\'s", " ")
data = data.replace("  ", " ").rstrip()

List= data.lower().split(" ") #소문자 통일 후 리스트로 쪼개기

SetL = sorted(list(set(List))) #중복제거 및 오름차순 정렬

index = 1 #단어 번호
print("==============================TEST1=======================================")
for i in range(len(SetL)):
    print(f"{index}. {SetL[i]}")
    index+=1

f.close()