import re
# []         : []사이의 문자들(어떤것이든)중 1개
# [from-to]  : 두 문자 사이 범위
# [^from-to] : 부정 [^0-9] (숫자 아닌 것)
# .          : 모든 문자 (\n제외)
# *          : 바로 앞 문자가 0회 이상 반복
# +          : 바로 앞 문자가 1회 이상 반복
# {m,n}      : 바로 앞 문자 m회 이상 n회 이하
# |          : or (바로 양끝 한 문자씩)
# ^          : "문자열" 시작 / 부정
# $          : "문자열" 끝
# ?          : 바로 앞문자 {0,1} (있거나 없거나)
# \          : 이스케이프 코드 / 메타 문자를 일반 문자로
# ()         : grouping, 추출할 패턴 지정

#자주 쓰는 문자 클래스 대용
# \d == [0-9]
# \D == [^0-9]
# \s ==  [ \t\n\r\f\v]
# \S == [^ \t\n\r\f\v] (whitespace 문자가 아닌 것)
# \w == [a-zA-Z0-9_] (문자+숫자(alphanumeric))
# \W == [^a-zA-Z0-9_] (문자+숫자(alphanumeric)가 아닌 문자)
# \b : word boundary (단어!만)
# \B : word boundary 아닌 것


#<정규표현식>
"""
import re
p = re.complie("ab*") --> 정규표현식 사용할 패턴 컴파일
m = p.search(str)
OR
import re
m = re.search("ab*", str)
"""

#match --> 문자열 처음에 매치 안되면 None, 1개만 찾음
#search --> 문자열 전체를 검색, 1개만 찾음, match 객체
#findall --> 패턴과 매치해서 리스트로 반환, 다찾음
#finditer --> findall과 비슷(반복가능한 객체 반환, 객체가 포함하는 각각은 match 객체)

p= re.compile("[a-zA-z]*")
result = p.finditer("life is too short")
#<callable_iterator object at 0x01F5E390>
for r in result: print(str(r).split())

"""
p = re.compile("[a-z]+")
m = p.match("python")
"""
# m.group() : 매치된 문자열을 반환
# m.start() : 매치된 문자열의 시작 위치 반환
# m.end() : 매치된 문자열의 끝 위치 반환
# m.span() : 매치된 문자열의 (시작, 끝)을 튜플로 반환

# re.DOTALL / re.S :  메타문자 “.” 은 \n 제외하고 match
# re.IGNORECASE or re.I :  대/소문자 구별없이 match
# re.MULTILINE or re.M : ^, $과 연관된 옵션
    # 문자열 처음/끝이 아니라 각 라인의 처음/끝에서도 match 하고 싶을 



#13p - want의 모든 활용형과 매칭
data = ["want", "wants", "wanted", "wanting", "Want", "Wants", "Wanted", "Wanting"]
p = re.compile("[Ww]ant.*")
for i in data:
    m = p.match(i)
    print(i,"--->", m)
    
#cat 찾고 싶으면 ----> 이거 다시 해라
data = ["cats", "cat's", "cat", "Cats", "Cat's", "Cat", "cat'"]
p = re.compile(r"[Cc]at['s]*(?!['])")
#r"cat('?s)?|Cat('?s)?"
#r"[Cc]at['s]*"
#r"cat['s]*|Cat['s]*"
#p = re.compile(r"[Cc]ats{0,1}") #개수를 조절하고 싶을 때 이렇게 쓰면 되겠지..???
#p = re.compile(r"C|cats{0,1}") #둘다 가능
for i in data:
    m = p.match(i)
    print(i,"--->", m)

#25p - 실습  give (활용형 포함) frequency 구하기
#give, gave, given, gives
f = open("C:\pythonpractice\EnglishProgramming_2\data\TheNorthWind&theSun2.txt", "r")
text = f.read()
data = text.split(" ")
matches = []
#data = ["give", "gave", "given", "gives", "Give", "Gave", "Given", "Gives"]
p = re.compile(r"\b([Gg]ive[n?|s?]?)\b|\b([Gg]ave)\b")
for i in data:
    m = p.search(i)
    if m !=None:
        matches.append(m.group())
print("give의 frequency는 -->", len(matches))
f.close()

#문자열 치환 : re.sub(old, new, data)
data = "abc-def"
re.sub("-", "#", data)
re.sub("-", "", data)
#re.subn(old, new, data) # 치환된 문자열과 치환된 개수가 들어 있는 튜플 리턴

#27p - 실습
data = "good morning, mr. smith. how are you? i'm fine, thank you. how's the weather outside? it's rainy today."
#문장 부호 모두 지우기
data2 = re.sub("('s)|,", "", data)

#문장 나누기
p = re.compile(r"\.|\?")
new_d = ""
for d in data2:
    if p.search(d):
        new_d += d + "\n"
    else:
        new_d +=d
sen = new_d.split("\n ")
sen[-1] = sen[-1].strip()
print(sen)

#첫글자 대문자
for i in range(len(sen)):
    sen[i] = sen[i][0].upper()+sen[i][1::]
print(sen)
