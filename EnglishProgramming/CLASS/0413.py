# update -> 다른 변수에 담지 마라..?? 확인 좀
#del 도 다른 변수에 담지 마라?
#keys() -> 새로운 자료형. dict_keys : 바꿀 수 없는 자료형이라서 list로 바꾸어서 활용함
#values() -> sort 못씀
#items() -> [(),()] 이렇게 튜플형태로 만든 리스트
#딕셔너리 정렬 : 딕셔너리는 원래 순서가 없는 자료형임.
# key, values, 쌍으로 정렬하는. 기준 이렇게 3가지.
#순서가 없응께 sort는 못씀. sort 쓰기 위해선 : key 찾고 -> list로 바꾸고 -> sortf

word = ["I", "love", "you", "very", "much", "!"]
#while word: --> word 안에 요소가 있으면 True
i = 0
while i < len(word)-1:
    print(word[i])
    i += 0

print("+"*30)

length = len(word)-1
while length <-1:
    print(word[length])
    length = -1

#initialize : i=0 이라고 초기화 하고 시작하는 것

while False :
    print("no")
print("yes")
#---> tes

#list 인덱스가 음수면 error가 뜨나???
#break는 loop 만 빠져나오는 예약어
#어떤 예약어는 loop뿐만 아니라 코드 자체에서 다 벗어나와서 종료하는 예약어도 있음.
#break를 유용하게 쓰기 위해서는 if 조건문을 알고 쓰면 더 좋아용 하지만 안배웠으므로... 이후에 유용할 것.
i=0
while True:
    print("~~")
    if i ==10:
        break

#중첩 loop은 원하는대로 잘 안되기 때문에, 잘 쓰지말자.
