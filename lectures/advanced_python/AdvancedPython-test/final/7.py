def personal_info(file, *want):
    want = list(want)
    #파일열고 읽는 함수
    def Read(file):
        f = open(file, "r")
        info = f.read()
        f.close()
        return info
    
    #주어진 데이터를 딕셔너리 형태로 바꿔주는 함수
    def makedict(info):
        group_L = info.split("\n\n")

        dict ={}

        for i in group_L:
            #name-key
            val = {}
            new = i.replace(": ", "\n")
            name = new.split("\n")[1]

            line = i.split("\n")
            for j in line:
                SmallList = j.split(": ")

                if "Age" in j:
                    val["age"]= SmallList[1]
                elif "Student_id" in j:
                    val["studentId"] = SmallList[1]
                elif "Location" in j:
                    val["location"] = SmallList[1]
                elif "Phone" in j:
                    val["phone"] = SmallList[1]

            dict[name] = val
                
        return dict

    #원하는 데이터를 처리해주는 함수
    def printwant(data):
        Want = []
        for i in want:
            if i == "Name":
                Want.append("name")
            elif i == "Age":
                Want.append("age")
            elif i == "StudentId":
                Want.append("studentId")
            elif i == "Location":
                Want.append("location")
            elif i == "Phone":
                Want.append("phone")
                
        pp = []
        for i in data:
            a = []
            for j in Want:
                if j == "name":
                    a.append(i)
                elif j == "age":
                    a.append(data[i]['age'])
                elif j == "studentId":
                    a.append(data[i]['studentId'])
                elif j == "location":
                    a.append(data[i]['location'])
                elif j == "phone":
                    a.append(data[i]['phone']) 
            sourc = ", ".join(a)
            pp.append(sourc)

        #출력
        for i in pp:
            print(i)

    data = Read(file)
    dictlist = makedict(data)
    printwant(dictlist)

print("함수 호출1")
personal_info("Personal_info.txt", "Name")
print("\n함수 호출2")
personal_info("Personal_info.txt", "Name", "Age")
print("\n함수 호출3")
personal_info("Personal_info.txt", "Name", "Age", "Phone")


