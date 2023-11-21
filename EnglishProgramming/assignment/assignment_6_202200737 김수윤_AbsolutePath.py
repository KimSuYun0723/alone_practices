with open("C:\\pythonpractice\\EnglishProgramming\\lily.txt", "r") as f:
    lily = f.read() # 파일 열기
    not_string = [".", ",", "\n"] 
    #제거할 문장부호, 및 이스케이프 시퀀스 리스트
    #언젠가 훨씬 다양한 문장부호를 처리할 수도 있다는 생각에, replace함수를 계속 나열하기엔 한계가 있다고 판단.
    num=0 #while문 실행 횟수를 제어할 변수

    while num < len(lily):
        for i in lily:
            for j in range(len(not_string)):
                if i == not_string[j]:
                    lily = lily.replace(f"{i}", "")
        num += 1 

    lilyList= lily.lower().split(" ") #initializing
    lilySetL = sorted(list(set(lilyList))) #중복제거 및 오름차순 정렬

    index = 1

    for i in range(len(lilySetL)):
        if index == 11:
            break

        c = lilyList.count(lilySetL[i])

        if c == 1:
            continue
        else:
            print(f"{index}. {lilySetL[i]}: {c}")
            index+=1