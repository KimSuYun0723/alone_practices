#2_reveiw(1)_18p
#임의의 숫자 2개를 input()을 통해 입력 받고, 두 숫자를 더하여 "Total: 숫자" 형식으로 출력하기
    #1 : 숫자를 한번에 1개씩 입력 받음
num1 = int(input("숫자를 1개 입력하세요: "))
num2 = int(input("숫자를 1개 더 입력하세요: "))
print(f"Total: {num1+num2}")

    #2 : 한번에 숫자 2개를 차례로 입력받기 (comma, space 등으로 구분)
num0 = input("숫자를 2개 입력하세요: ")
answer = num0.replace(" ","").split(",")
print(answer)
sum = 0
for i in answer:
    sum += int(i)
print(f"Total: {sum}")

#Slicing_19p
    #[1:] == [1::]
    #처음부터 9까지_ [:10] == [:10:] 

#내장함수(20p)
    #lower, upper으로 안바뀌면 적어도 영어는 아니라고 확인 가능
    #길이 = index +1

#List 요소 +(25p)
a = [1,2,3]
b = [10,20,30]

print(a+b) #a+=b #[1, 2, 3, 10, 20, 30]
    #a.append()
print(a.append(b)) #None
a = [1,2,3]
a.append(b)
print(a) #[1, 2, 3, [10, 20, 30]]
    #a.extend()
print(a.extend(b)) #None
a = [1,2,3]
a.extend(b)
print(a) #[1, 2, 3, 10, 20, 30]
    #a.insert()
print(a.insert(0, b)) #error _ argument 2개 필요
a = [1,2,3]
a.insert(0, b)
print(a) #[[10, 20, 30], 1, 2, 3]


#List 요소 -(27p)
    #a.remove()
a.remove(1) #가장 처음 발견된 요소
    #a.pop()
a.pop() #가장 마지막 요소 pop
a.pop(2) #인덱스로 삭제
    #a.clear()
a.clear() #자료형은 남아있고, 요소 모두 삭제
    #del a[]
del a[2] #인덱스로 삭제

#Tuple(31p)
    #정렬하고 싶을 때 --> sorted (sort X)

#Set(33p)
    #집합 연산시 합집합 --> | (or 이랑 연산 결과 다름)
    
#Dictionary(39p)
    #key 존재하는지 확인 --> in
    #values --> .values & in 사용 / loop 돌면서 key 넣으면서 순회
    #.keys(), .values(), .items()
    #sorted() --> key 목록은 순서를 보장하지 않음
    #sort()
    #key 기준으로 정렬 -> sorted(dic.keys())
    #value 기준으로 정렬 -> sorted(dic.values())
    #key:value 쌍으로 정렬
"""
#1
import operator
sorted(ages.items(), key = operator.itemgetter(1)) #1 value 기준, 0 key 기준, reverse=True
#2
sorted(ages.items(), key=lambda x:x[1]) #1 value 기준, 0 key 기준, reverse=True
"""