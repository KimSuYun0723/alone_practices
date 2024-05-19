# 2 - 1)

def mydelete(List, idx):  #List: 삭제할 요소가 들어 있는 리스트  #idx: 삭제할 인덱스 번호
    answer = []
    for i in List:
        if i != List[idx]:
            answer.append(i)
    return answer