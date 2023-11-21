print("==============실습===============")

gpa = input("GPA를 입력하세요. : ")
grade = input("학년을 입력하세요. : ")
subject = input("이수학점을 입력하세요. : ")

#if문
if (int(grade) ==4) and (gpa>=4.0) and (subject>=12):
    print("장학금 신청 대상자입니다.")
elif (gpa>=4.0) and (subject>=17) and ():
    print("장학금 신청 대상자입니다.")
else:
    print("장학금 신청 대상자가 아닙니다.")

#중첩구문1
if int(grade) ==4:
    if (gpa>=4.0) and (subject>=12):
        print("장학금 신청 대상자입니다.")
elif (gpa>=4.0) and (subject>=17) and ():
    print("장학금 신청 대상자입니다.")
else:
    print("장학금 신청 대상자가 아닙니다.")

#중첩구문2
if gpa>=4.0:
    if int(subject)==4:
        if subject>=12:
            print("장학금 신청 대상자입니다.")
        else:
             print("장학금 신청 대상자가 아닙니다.")
    else:
        if subject>=17:
            print("장학금 신청 대상자입니다.")
        else:
            print("장학금 신청 대상자가 아닙니다.")
else: 
    print("장학금 신청 대상자가 아닙니다.")
