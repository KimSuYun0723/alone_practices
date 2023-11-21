with open("lily.txt", "r") as f:
    lily = f.read() # 파일 열기
    not_string = [".", ",", "\n"] #제거할 문장부호, 및 이스케이프 시퀀스 리스트
    #언젠가 훨씬 다양한 문장부호를 처리할 수도 있다는 생각에, replace함수를 계속 나열하기엔 한계가 있다고 판단.
    
    num=0 #while문 실행 횟수를 제어할 변수

    while num < len(lily):
        for i in lily:
            for j in range(len(not_string)):
                if i == not_string[j]:
                    lily = lily.replace(f"{i}", "")
        num += 1 

    lilyList= lily.lower().split(" ") #소문자 통일 후 리스트로 쪼개기
    lilySetL = sorted(list(set(lilyList))) #중복제거 및 오름차순 정렬

    index = 1 #단어 번호

    for i in range(len(lilySetL)):
        if index == 11: # 10개까지만 출력
            break

        c = lilyList.count(lilySetL[i]) #중복제거하여 연산 감소

        if c == 1:
            continue #continue 활용
        else:
            print(f"{index}. {lilySetL[i]}: {c}")
            index+=1




"""
처리를 하다보면 3개문장이 아니라 4.가 생길수도있는데, 그걸 생각하면서 하기
4.가 X
문장 앞에 띄어쓰기를 없애도록
"""