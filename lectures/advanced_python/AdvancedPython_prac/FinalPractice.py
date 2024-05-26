f = open("Personal_info.txt", "r")
info = f.read()
f.close()

group_L = info.split("\n\n") #뭉탱이
dict ={}
for i in group_L:
    #{이름:정보}
    
    
    #name-key
    val = {}
    new = i.replace(": ", "\n")
    name = new.split("\n")[1]

    #info-value 완성
    line = i.split("\n")
    for j in line:
        SmallList = j.split(": ")

        if "Age" in j:
            val["age"]= int(SmallList[1])
        elif "Student_id" in j:
            val["studentId"] = int(SmallList[1])
        elif "Location" in j:
            val["location"] = SmallList[1]
        elif "Phone" in j:
            val["phone"] = SmallList[1]

    dict[name] = val

print(dict) 

"""
{'Kim Minju': {'age': 22, 'studentId': 20211020, 'location': 'Seoul, South Korea', 'phone': '010-1234-5678'}, 
'Lee Jihyun': {'age': 20, 'studentId': 20222021, 'location': 'Busan, South Korea', 'phone': '010-9876-5432'}, 
'Park Hyunwoo': {'age': 25, 'studentId': 20201022, 'location': 'Incheon, South Korea', 'phone': '010-5555-5555'}, 
'Choi Soomin': {'age': 21, 'studentId': 20221023, 'location': 'Gwangju, South Korea', 'phone': '010-1111-2222'}, 
'Kang Jaewon': {'age': 23, 'studentId': 20211024, 'location': 'Daegu, South Korea', 'phone': '010-9999-8888'}}
"""

#################################################
print("===================================================================")
def personal_info(file, *want):
    want = list(want)

    def Read(file):
        f = open(file, "r")
        info = f.read()
        f.close()
        return info
    
    def makedict(info):
        group_L = info.split("\n\n") #뭉탱이

        #{이름:정보}
        dict ={}

        for i in group_L:
            #name-key
            val = {}
            new = i.replace(": ", "\n")
            name = new.split("\n")[1]

            #info-value 완성
            line = i.split("\n")
            for j in line:
                SmallList = j.split(": ")

                if "Age" in j:
                    val["age"]= int(SmallList[1])
                elif "Student_id" in j:
                    val["studentId"] = int(SmallList[1])
                elif "Location" in j:
                    val["location"] = SmallList[1]
                elif "Phone" in j:
                    val["phone"] = SmallList[1]

            dict[name] = val
                
        return dict

    def printwant(data):
        Want = []
        for i in want:
            if i == "이름":
                Want.append("name")
            elif i == "나이":
                Want.append("age")
            elif i == "학번":
                Want.append("studentId")
            elif i == "위치":
                Want.append("location")
            elif i == "전화번호":
                Want.append("phone")
                
        answer = {}

        if (len(want)==1) and (want[0] == "이름"):
            return list(data.keys())
        else:
            for i in data:
                val = {}
                for j in Want:
                    val[j] = data[i][j]
                answer[i] = val

            answer_L = []
            for i in answer:
                print(f"{i} : {answer[i]}")
                answer_L.append(f"{i} : {answer[i]}")
            return answer_L
                      

    data = Read(file)
    dictlist = makedict(data)
    printwant(dictlist)

personal_info("Personal_info.txt", "나이", "위치")
    

"""
{'Kim Minju': {'age': 22, 'studentId': 20211020, 'location': 'Seoul, South Korea', 'phone': '010-1234-5678'}}
{'Lee Jihyun': {'age': 20, 'studentId': 20222021, 'location': 'Busan, South Korea', 'phone': '010-9876-5432'}}
{'Park Hyunwoo': {'age': 25, 'studentId': 20201022, 'location': 'Incheon, South Korea', 'phone': '010-5555-5555'}}
{'Choi Soomin': {'age': 21, 'studentId': 20221023, 'location': 'Gwangju, South Korea', 'phone': '010-1111-2222'}}
{'Kang Jaewon': {'age': 23, 'studentId': 20211024, 'location': 'Daegu, South Korea', 'phone': '010-9999-8888'}}
"""    

#여러개 받을 수 있게도 해봐


#데이터에서 이름만 출력


# 나이순으로 이름과 나이출력


# 특정학번인사람만 출력


