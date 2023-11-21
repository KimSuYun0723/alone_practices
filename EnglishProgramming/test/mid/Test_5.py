word_1 = ['apple', 'banana', 'orange', 'grape', 'pineapple']
word_2 = ['pear', 'kiwi', 'watermelon', 'strawberry', 'peach']

#1. 5가지 방법으로 word_1 + word_2
print("=============== 1. ===============")
#append, insert(index 번호를 가지고 붙이는 아이), extend, +, +=, set도 가능하지만(if나 반복문을 사용하지 않는다면 비추: 순서가 달라지기 때문)
print("\n====== (1)+연산자 ======")
word01 = word_1 + word_2
print(word_1)
print(word_2)
print(word01)

print("\n\n====== (2)+= 연산자 ======")
word1 = word_1
word2 = word_2
word1 += word2

print(word_1)
print(word_2)
print(word1)

print("\n\n====== (3)extend ======")
word03 = word_1
word04 = word_2
word03.extend(word04)
print(word_1)
print(word_2)
print(word03)

print("\n\n====== (4) append ======")
word05 = word_1
word06 = word_2
#이것도 반복문이랑 쓰면 되잖아 이색기야 ㅜㅜㅜㅜㅜㅜㅜㅜㅜ
word05.append(word06[0])
word05.append(word06[1])
word05.append(word06[2])
word05.append(word06[3])
word05.append(word06[4])

print(word_1)
print(word_2)
print(word05)

print("\n\n====== (5)pop ======")
word07 = word_1
word08 = word_2
a = word08.pop()
b = word08.pop()
c = word08.pop()
d = word08.pop()
e = word08.pop()
word07.append(a)
word07.append(b)
word07.append(c)
word07.append(d)
word07.append(e)


#2. 병합된 리스트 안에 들어있는 단어들의 길이를 구하여, 단어 길이의 오름차순으로 단어를 출력
    #while을 쓰라고 이색갸...;;;;
print("\n\n=============== 2. ===============")
dict = {}

dict[word01[0]]= len(word01[0])
dict[word01[1]]= len(word01[1])
dict[word01[2]]= len(word01[2])
dict[word01[3]]= len(word01[3])
dict[word01[4]]= len(word01[4])
dict[word01[5]]= len(word01[5])
dict[word01[6]]= len(word01[6])
dict[word01[7]]= len(word01[7])
dict[word01[8]]= len(word01[8])
dict[word01[9]]= len(word01[9])
print(dict)

a= sorted(dict.items(), key=lambda x: x[1]) 
print(a[0][0])
print(a[1][0])
print(a[2][0])
print(a[3][0])
print(a[4][0])
print(a[5][0])
print(a[6][0])
print(a[7][0])
print(a[8][0])
print(a[9][0])


