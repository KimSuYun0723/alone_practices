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
def getnum(phonenum, sep=", ", num=0):
    ###################3
    phonenum0 = phonenum.split("\n")
    List = []

    for i in phonenum0:
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

    ################################
    if num ==0:
        for i in range(len(answerreal)):
            print(answerreal[i], end=sep)
            if i == len(answerreal)-1:
                print(answerreal[i])
    elif num > len(answerreal):
        print("추출을 원하는 번호의 개수가 알맞은 전화번호의 개수보다 더 큽니다. 알맞은 번호를 전체를 출력합니다.")
        for i in range(len(answerreal)):
            print(answerreal[i], end=sep)
            if i == len(answerreal)-1:
                print(answerreal[i])
    else:
        for i in range(num):
            print(answerreal[i], end=sep)
            if i == len(answerreal)-1:
                print(answerreal[i])        

print("함수 호출1")
getnum(phone_num, num =20)
print("\n함수 호출2")       
getnum(phone_num, sep="\n")
