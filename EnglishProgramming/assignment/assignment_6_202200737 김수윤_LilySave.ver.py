"""
Data : lily.txt
단어 번호, 단어 목록, 단어 빈도수 출력
오름차순 정렬
단어빈도 1이면 출력 안함(continue) 사용
10번째 단어까지 출력
1. a:8
2. adventure: 2
3. an: 2
"""

with open("C:\\pythonpractice\\EnglishProgramming\\lily.txt", "r") as f:
    lily = f.read()
    not_string = [".", ",", "\n"]
    num=0

    while num < len(lily):
        for i in lily:
            for j in range(len(not_string)):
                if i == not_string[j]:
                    lily = lily.replace(f"{i}", "")
        num += 1 

    lilyL= lily.split(" ")
    proper = ["Lily"]
    list = []
    for i in range(len(lilyL)):
        for j in range(len(proper)):
            if lilyL[i] != proper[j]:
                if lilyL[i] != lilyL[i].lower():
                    lilyL[i] = lilyL[i].lower()

    lilyL.sort()
    print(lilyL)
