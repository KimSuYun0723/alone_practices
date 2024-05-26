#문제1 - 숫자 하나를 1개씩
"""
a = int(input("(1) 숫자 하나를 입력하세요: "))
b = int(input("(2) 숫자 하나를 더 입력하세요: "))
"""

#문제2 - 숫자 2개를 차례로
a = input("(1) 숫자 2개를 입력하세요: ")

def ReturnNum(a):
    b = a.split(",")
    if " " in a:
        b.remove(" ")
    one = b[0]
    two = b[1]
    return one, two

print(ReturnNum(a))

dic = {"a":2, "c":3, "d":1, "b":2}
dic1 = sorted(dic.keys())
#dic2 = sorted(dic.values())
#dic3 = sorted(dic.items())

print(dic1)
print(list(dic.keys()))
#print(dic2)
#print(dic3)


    #key:value 쌍으로 정렬
"""
#1
import operator
sorted(ages.items(), key = operator.itemgetter(1)) #1 value 기준, 0 key 기준, reverse=True
#2
sorted(ages.items(), key=lambda x:x[1]) #1 value 기준, 0 key 기준, reverse=True"""