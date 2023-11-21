alice = """Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes."""

#1. 데이터에 대한 단어 목록 만들기 --> 소문자로 만들었어야 했나...
print("========== 1. WORDS LIST ==========")
clean_alice = alice.replace(",","").replace("\"", "").replace(".", "")
words = clean_alice.split(" ")
words_list = list(words)
print(words_list, "\n")

#2. 오름차순 정리
print("========== 2. sort ==========")
arrange = sorted(words_list)
print(arrange, "\n")

#3. set 함수로 중복요소 삭제하기
print("========== 3.NO SAME ==========")
alice_set = set(words_list)
print(alice_set, "\n")

#4. 단어 목록 출력하기
print("========== 4. WORDS LIST ==========")
print(list(alice_set), "\n")


