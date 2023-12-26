#<대소문자 변환>
# str.swapcase() : 대소문자 상호변환
# str.title() : 각 단어 제일 앞글자 대문자로 변환
ss = "python is Easy. 재미있는 programming"

#<문자열 구성파악 -T/F 반환>
# str.isdigit( ) : 전체가 숫자(문자로된 숫자)로만 구성되어 있는가
# str.isalpha( ) : 전체가 글자(한글/영어)로만 구성되어 있는가
# str.isalnum( ) : 전체가 글자 또는 숫자(문자로된 숫자)로 섞여서 구성되어 있는가
# str.islower( ) : 전체가 소문자로만 구성되어 있는가(숫자 OK)
# str.isupper( ) : 전체가 대문자로만 구성되어 있는가(숫자 OK)
# str.isspace( ) : 전체가 공백문자(\t,\n," "포함)로만 구성되어 있는가

#4p - 실습
Data = "A machine-readable lexical database organized by MIT Technology Review in 2000 !!!!"
"""위 데이터에 대해 isdigit( ) isalpha( ) isalnum( ) islower( ) isupper( ) isspace( ) 해보기"""
#고려 대상 == 대문자 / 소문자 / 숫자 / 기호 / 공백
# 대문자로 되어 있는 단어
up = [] #['A', 'MIT']
for i in Data.split():
    if i.isupper():
        up.append(i)

# 대+소문자로 되어 있는 단어 찾기
uplo = [] #['Technology', 'Review']
for i in Data.split():
    if (i.isupper()==False) and (i.islower()==False):
        if i.isdigit() == False: #2000빼주기 + 기호 어쩔건디(i.isalnum()도 False!!!)
            uplo.append(i)
print(uplo)
# 기호를 포함한 단어 찾기
symbol = [] #['machine-readable', '!!!!']
for i in Data.split():
    if i.isalnum()==False:
        symbol.append(i)

# 숫자로 된 단어 찾기
onlynum = [] #['2000']
for i in Data.split():
    if i.isdigit():
        onlynum.append(i)
print(onlynum)

#<문자열 찾기>
# .count(str) : 찾을 문자열(str)이 몇 개 들었는지 개수를 셈
# .find(str) : 찾을 문자열의 인덱스 반환
# .find(‘찾을 문자열’, 시작위치): 지정한 시작위치부터 문자열을 찾고 인덱스 반환
# .rfind(str) : 오른쪽부터 찾음
# .index(str) : find() 함수와 동일한 용도, 찾을 문자열이 없다면 오류가 발생 (find()는 -1)
# .startswith(str) : 찾는 문자열로 시작하면 True를, 그렇지 않으면 False를 반환
# .endswith(str) : 찾는 문자열로 끝나면 True를, 그렇지 않으면 False를 반환
s = "Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32"


#<문자열 공백제거>
# strip(), rstrip(), lstrip() :공백 혹은 지정한 문자 제거
    #중간에 있는 것은 제거되지 않음
    #첫번째 공백 X / 첫글자가 공백이어야 작용
ss1 = " 파 이 썬 "
ss2 = "#####파#####이#####썬#####"


#<문자열 분리, 결합>
# split() : 문자열을 공백이나 다른 문자로 분리해서 리스트를 반환
# splitlines() : 행 단위로 분리
# a.join(b) : 문자열 b에 포함된 문자 사이에 문자열 a가 삽입
ss = "하나\n둘\n셋 \n "
a = ss.splitlines()
print(a)

# 8p - 실습(TheNorthWind&theSun.txt)
"""read()로 파일 읽은 다음 단락 나누기)"""
f = open("C:\pythonpractice\EnglishProgramming_2\data\TheNorthWind&theSun.txt", "r")
data = f.read()
para = data.splitlines()
for i in para:
    print(i)
    print()
f.close()


#map()
before = ["2023", "12", "24"]
after = map(int, before)
print("1", after) #map은 그냥 출력하면 주소가 뜸 <map object at 0x000002A84E3DBA60>

after = list(after)
print("2", after)

a = input().split() #공백으로 split
print("3", a)
a = list(map(int,a))
print("4", a)
print(a==after) 


#<문자열 정렬 및 채우기>
# str.center(숫자) : 숫자만큼 전체 자릿수를 잡은 후 문자열을 가운데 배치
# str.ljust(숫자) : 왼쪽에 붙여 출력
# str.rjust(숫자) : 오른쪽에 붙여 출력
# str.zfill(숫자) : 오른쪽으로 붙여 쓰고 왼쪽 빈 공간은 0으로 채움
ss = "파이썬"
print("!",ss.rjust(6),"!")

#11p - 실습(문장 나누기)
data = "Good morning, Mr. Smith. How are you? I'm fine, thank you. How's the weather outside? It's rainy today."




