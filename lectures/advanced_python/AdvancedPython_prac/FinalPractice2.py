#데이터에서 이름만 출력
print("============================이름 출력======================================")
def personal_info(file):

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

    def printname(data):
        #나이를 리스트로 먼저 만들고 sort
        print(list(data.keys()))


    data = Read(file)
    dictlist = makedict(data)
    printname(dictlist)

personal_info("Personal_info.txt")

# 나이순으로 이름과 나이출력
print("\n\n=============================나이순 출력======================================")
def personal_info(file):

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

    def printage(data):
        #나이를 리스트로 먼저 만들고 sort
        agelist = []
        for i in data:
            agelist.append(data[i]['age'])
            agelist = sorted(agelist) #reverse = 1

        #sort된 리스트 하나씩 참조하면서 나이 같으면 이름 출력
        for i in agelist:
            for j in data:
                if data[j]['age'] == i:
                    print(f"{j} : {i}")


    data = Read(file)
    dictlist = makedict(data)
    printage(dictlist)

personal_info("Personal_info.txt")

# 특정학번인사람만 출력
print("\n\n=============================특정 학번인 사람 출력======================================")
def personal_info(file, id):

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

    def printid(data, id):
        for i in data:
            if data[i]['studentId'] == id:
                print(f"{id}: {i}")

    data = Read(file)
    dictlist = makedict(data)
    printid(dictlist, id)

personal_info("Personal_info.txt", 20211020)

"""
{'Kim Minju': {'age': 22, 'studentId': 20211020, 'location': 'Seoul, South Korea', 'phone': '010-1234-5678'}, 
'Lee Jihyun': {'age': 20, 'studentId': 20222021, 'location': 'Busan, South Korea', 'phone': '010-9876-5432'}, 
'Park Hyunwoo': {'age': 25, 'studentId': 20201022, 'location': 'Incheon, South Korea', 'phone': '010-5555-5555'}, 
'Choi Soomin': {'age': 21, 'studentId': 20221023, 'location': 'Gwangju, South Korea', 'phone': '010-1111-2222'}, 
'Kang Jaewon': {'age': 23, 'studentId': 20211024, 'location': 'Daegu, South Korea', 'phone': '010-9999-8888'}}
"""  
