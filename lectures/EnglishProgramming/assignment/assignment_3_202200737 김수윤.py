alice = """Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes."""

#**데이터 정제화(문장 부호 전부 제거 먼저하기)
#원본데이터는 훼손하지 말고, 나중에 파일 형태의 자료가 주어져도 그렇게.
#데이터가 바뀌어도 동일하게 찾을 수 있게, 소프트 코딩을 할 것.
#리스트는 중간에 요소를 뗴어내는게 가능하지만, string은 del 못씀. 
#그래서 리스트로 바꿔서 하고, join
#str(a) 함수 쓰면 되지 않나요? -> 아니, join처럼 되는게 아니라 리스트 자체가 sting으로 바뀜 "[]" 이렇게/
#아니면 해당 요소를 찾아서 n번째 인덱스 제외하고 갖다 붙여
#replace(old, new, count) -> 원래는 count에 숫자 집어넣으면 왼쪽에서 count개 만큼만 바꿔줌.
#문장부호가 있는 단어는 단어가 아니다.

clean_alice = alice.replace(",", "").replace(".", "").replace("\"", "")
print(clean_alice, "\n")

#1. 전체 단어 개수 구하기
print("========== 1. LENGTH OF WORDS ==========")
print(len(clean_alice), "\n")

#2. 단어 she가 몇 번 등장하는지 구하기
print("========== 2. HOW MANY SHE ==========")
alice1 = clean_alice
low = clean_alice.lower() #text normalization
she_num = low.count("she")
print(she_num, "\n")


#3. 띄어쓰기를 모두 “=”로 바꾸기 • split과 join 쓰기
print("========== 3. BLANK->'=' ==========")
alice2 = alice
blank = alice2.split(' ')
blank_print = '='.join(blank)
print(blank_print, "\n")

#4. 문장부호 중 처음으로 등장한 온 점만 지우기
print("========== 4. DLETE FIRST '.' ==========")
alice3 = list(alice)
alice3.remove('.')
alice4 = ''.join(alice3)
print(alice4, "\n")

#2
print("========== 4-2. DLETE FIRST '.' ==========")
index = alice.find('.')
alice5 = alice[:index] + alice[index+1:]
print(alice5, "\n")

#5. 처음으로 등장한 단어 of를 in으로 바꾸기 (문법성 x)
print("========== 5. FIRST OF -> 'in' ==========")
alice05 = alice.replace('of', 'in', 1)
print(alice05, "\n")


#6. 첫 번째 단어 추출하고 출력하기 • pop 사용
print("========== 6. FIRST WORD PRINT ==========")
alice06 = clean_alice.split(" ")
word_alice = list(alice06)
first = word_alice.pop(0)
print(first, "\n")


#7. 마지막 5개 단어만 추출하기
print("========== 7. PRINT LAST 5 WORDS ==========")
alice07 = clean_alice.split(" ")
word_alice = list(alice07)
print(word_alice[-5:], "\n")

#8. 데이터 전체를 역순으로 출력하기
print("========== 8. WORDS LENGTH ==========")
print(alice[::-1], "\n")

#**pop을 쓸 땐 원본 데이터가 훼손되므로 주의!
