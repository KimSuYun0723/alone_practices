phone_num = """02-933-432

 

109-123-4085

 

02-053-268

 

02-693-720

 

110-534-6401

 

02-427-9336

 

02-8201-6552

 

02-2936-219

 

911-353-4294

 

02-386-919

 

02-118-805

 

02-1501-021

 

02-3358-3194

 

02-892-306

 

02-876-152

 

02-6089-6775

 

02-5294-386

 

02-7614-0834

 

012-477-1784

 

080-5941-4919

"""
def getnum(num):
    num = phone_num.split("\n")
    List = []

    for i in num:
        if len(i) > 1:
            List.append(i)

    answer = []
    for i in List:
        Use = i.split("-")
        if (len(Use[1])>=3) and (len(Use[1])<=4):
            if (Use[0] == "02") and (len(Use[2]) == 4):
                answer.append(i)
            elif (Use[0] == "02") and (len(Use[2]) == 3) and (len(Use[1])==4):
                answer.append(i)
    answerreal =[]
    for i in answer:
        Use = i.split("-")
        if len(Use[2]) ==4:
            answerreal.append(i)
        elif len(Use[2])==3:
            Use2 = "".join(Use)
            Use2 = f"{Use2[0:2]}-{Use2[2:5]}-{Use2[5::]}"
            answerreal.append(Use2)

    return answerreal

print(getnum(phone_num))