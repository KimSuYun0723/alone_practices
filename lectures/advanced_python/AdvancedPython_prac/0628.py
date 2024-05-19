a = ["banana", "kiwi", "apple", 1,2,3]
print(a[0][2])
b = list(a[0])[2] = "n"
a[0] = b
print(a[0])


print("==============실습===============")
data_1 = "Once upon a time, there was a young man named Jack who lived in a small village."
data_2 = "He was a curious and adventurous person who loved exploring the world around him."

data1 = data_1
data2 = data_2

#• 데이터 각각의 글자수 세기 80, 81
Data1 = data1.replace(",", "").replace(".", "")
Data1 = Data1.split(" ")
Data2 = data1.replace(".", "")
Data2 = Data1.split(" ")
print(len(data1))
print(len(data2))

#• 단어수 세기 17, 14 : 글자수는 비슷한데, 단어수가 작은 것을 보면 단어가 전반적으로 좀 길다는 것을 알 수 있음(단정할순 없지만)
Data1 = data1.replace(",", "").replace(".", "").lower()
Data1 = Data1.split(" ")
Data2 = data1.replace(".", "").lower()
Data2 = Data1.split(" ")
print(len(Data2))

#• 문장부호 지우기
Data1 = data1.replace(",", "").replace(".", "")
Data2 = data1.replace(".", "")
print(Data1)
print(Data2)

#• 모두 소문자로 만들기
Data1 = data1.lower()
Data2 = data1.lower()

#• data1과 data2 병합
print(data1+data2) #를 하면, .으로 붙어있으니까;; 뉴라인이나 띄어쓰기를 중간에 넣어줘야해..
# 문자열끼리 결합해봐!! 했을 때 컴마(,)로 프린트하면, 말그대로 출력만 되는 것. 변수에 할당해서 데이터로 활용해볼수가 없음.
#결합해보라고 하면 그래서 +같은것을 활용해야 함.


d4 = data1[:]#d1[:]
#d4.extend(d2)
print(d4) #None 
#-> 한줄로 쓸수가 없는 애들... 따로따로 해줘 (????)

#• 문자열
#• 리스트

