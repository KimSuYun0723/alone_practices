f = open("Personal_info.txt", "r")
info = f.read()

info1 = info.replace("\n\n", "\n")
name = info1.split("\n")
print(name[0::5])
List = "".join(name[0::5])
List = List.split("Name: ")
print(List[1::])

"""
for d in data_list:
    if "Name" in d:
        print(d)


- 이름은 항상 나이위.
아니면 -.6.12.18 이럴떄 이름이 있음
- 다른 줄은 : 있는데 이름에는 없고, 뉴라인에 없음. 활용해서 -> 1. 뉴라인을 없앤다 2. 콜론 없는 줄 중에서 글씨가 써져있는 줄(len이 무조건 0 이상)
- 앞에 구분자 없을 때, 배수의 개념을 쓰지말고..> 학번을 찾아서(8자리라던가, int로 바꿔서 200이상 이런거)
- 뉴라인 없다고 치면.. 숫자 2자리 앞에 2개가 이름이다 뭐 이런식으로 
어떤 데이터가 있어도 찾을 수는 있음. 규칙을 찾아서 원하는 정보에 접근
"""
f.close()