#집합 : {}
"""
- 중복요소 포함 불가능
- 요소 순서 없음
- 인덱스 번호로 접근 불가(sequence type이 아니잖아~)
- 순서대로 되어있는 것 같을 때.. 우연의 일치임.
- 합.교.차집합 같은 연산 가능

• 차집합: - 연산자 사용
f3 = f1 – f2
• 합집합: | 연산자 사용 (or)
f4 = f1 | f2
• 교집합: & 연산자 사용 (and)
f5 = f1 & f2
"""

#set(리스트/튜플) --> assignment4
"""
- 중복되는 요소 제거, 유니크한 요소만 남길 수 있음
- 텍스트 안에 등장하는 단어 중 중복되는 단어를 정리하는데 유용하게 사
용 가능
- 순서가 없어서 순서 필요한 목록 관리 불편
- 순서 만들기 위해서 -> list(튜플/집합)
a = list(set(a))
==> sort() X(원본 훼손)
==> sorted(list(set(a))) <-- 원본 유지
"""

#리스트.튜플.집합
"""
- 모두 목록 형태 자료형
"""

#딕셔너리 : {}
"""
    : key & value의 쌍
- 순서 X --> key로 접근
- index num X
- 새로운 값 입력/딕셔너리 요소 참조 시, 대괄호[] 이용
- 특정 요소 변경 시에도 key 이용
"""
print("========== dictionary ==========")
word = {"apple": "사과", "ant": "개미"}
print(word["apple"])
word["bee"] = "벌" #순서가 마지막에 들어갔다면 우연임.
print(word)

age = {}
age["Park"] = 20
age["Lee"] = 21
age["Kim"] = 22
print(age)

age["Kim"] = 25
age["aaa"] = 0
print(age)



#포함 연산자(in/not in)
"""
    : 데이터 안에 찾고자 하는게 있는지 확인
- 연산 결과는 bool
- string/list/tuple/set/dict 모두 사용 가능
- dict에서 사용시 key에만 접근 가능
"""
print("========== in(key 존재 확인) ==========")
print("Kim" in age) #T

print("=== string ===")
a = "apple pie"
print("a" in a) #T
print("f" in a) #F

print("=== list ===")
b = ["apple", "pie"]
print("apple" in b) #T
print("a" in b) #F

print("=== tuple ===")
c = ("apple", "pie")
print("apple" in c)
print("a" in c)
print("a" in c[0])

print("=== set ===")
d = {"apple", "pie"}
print("apple" in d)
print("a" in d)

print("=== dict ===")
e = {"apple": 1, "pie": 2}
print("apple" in e)
print("a" in e)

#딕셔너리변수.update(결합할 딕셔너리)
"""
    : 딕셔너리 결합
- 에러는 안나지만 할당 X
"""

print("========== update() ==========")
word1 = {"apple": "사과", "ant": "개미"}
word2 = {"bee": "벌", "cat": "고양이"}
word1.update(word2) #word1 바뀜.
print(word1)
print(word2)
word3 = word1.update(word2)
print(word3) #None
print(type(word1.keys())) #<class 'dict_keys'>
print(word1.keys()) #dict_keys(['apple', 'ant', 'bee', 'cat'])
print(list(word1.keys())) #['apple', 'ant', 'bee', 'cat']

#del 딕셔너리[key] : 요소 삭제, 할당 error

#딕셔너리.keys()
"""
    : 딕셔너리에서 key 목록을 얻는 함수
- keys()로 반환되는 값의 자료형은 dict_keys
    - (자료형이 따로있음) 근데 바꿀수 없는 자료형.
    #list.(word1.keys()) --> 이렇게 list 바꿔서 활용
"""

#딕셔너리.values() : value 목록 얻기 -> 자료형 dict_keys

#딕셔너리.items() : key와 value의 조합을 튜플로 만든 목록 얻기
    # -> 자료형 dict_keys

#딕셔너리 정렬 --> key정렬/value정렬/쌍으로 정렬
"""
1. key 목록 정렬
    1) sorted(age.keys())
    2) age_k = list(age.keys())
        age_k.sort()
        print(age_k) 
        # sort()랑 print 한줄에 불가
    *  age.keys().sort() -> X, sorted 면 가능
#key -> list -> set

2. value 목록 정렬
    1) print(sorted(age.values()))
    2) age_v = list(age.values())
       age_v.sort()
       print(age_v)

3. key:value 쌍으로 정렬 *sort는 안돼~
    1) key 기준
        >>> sorted(age.items()) #내림차순은 reverse=True
    
    2) value 기준

(1) operator.itemgetter
import operator
sorted(ages.items(), key= operator.itemgetter(1))
#여기서 key는 딕셔너리 키 가 아님.
#1 value 기준, 0 key 기준
# 내림차순 reverse=True

(2)lamda
sorted(ages.items(), key=lambda x: x[1]) #1 value 기준, 0 key 기준
# 내림차순 reverse=True
"""

