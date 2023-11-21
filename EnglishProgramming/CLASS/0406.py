alice = """Alice, a girl of seven years, is feeling bored and drowsy while sitting on the riverbank with her elder sister. She then notices a talking, clothed White Rabbit with a pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious hall with many locked doors of all sizes. She finds a small key to a door too small for her to fit through, but through it she sees an attractive garden. She then discovers a bottle on a table labelled "DRINK ME," the contents of which cause her to shrink too small to reach the key which she has left on the table. She eats a cake with "EAT ME" written on it in currants as the chapter closes."""

#위 데이터에 대해 단어 목록을 만들기
alice1 = alice.lower()
alice1 = alice.replace(".","").replace(",","").replace("\"","")
print(alice1)
alice_list = alice.split(' ')

#오름차순으로 정리하기
alice_list_1 = alice_list.sort()

#set 함수를 통해 중복되는 요소 삭제하기
set = set(alice_list_1)

#단어 목록 출력하기
print(set)

