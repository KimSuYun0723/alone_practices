print("==========8-1번 문제==========")
score = {"국어":85, "수학":49, "과학":69, "영어":76}

print("###8-1번 :\n ", sorted(score.items(), key=lambda x: x[1], reverse = True))


print("\n\n==========8-2번 문제==========")

val = list(score.values())
av = sum(val)/len(val)
print("###8-2번 : ")
if av >= 60:
    print(str(av)+"점으로 합격입니다")
else:
    print(str(av)+"점 차이로 불합격입니다")


