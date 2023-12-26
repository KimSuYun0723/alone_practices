#13p_want의 모든 활용형과 매칭되게 하려면?
import re
p = re.compile("want.*")
#p = re.compile(r"[Ww]an(ts?)|(ed)|(ing)")
string = ["want", "wants", "wanted", "wanting", "Wanting"]

for s in string:
    m = p.search(s)
    #m은 매치된 단어만 알려주는게 아니라 다양한 정보를 다알려주는 아이임.
    #search는 다 찾아주지 않고 1개만 찾아줘 그래서 for문 필요
    if m:
        print(s, "YES")
    else:
        print(s, "NO")
        
        
p = re.compile(r"[Ww]ant(s?)|(ed)|(ing)") #괄호를 해줬으니 이렇게 되는거지, 괄호 안하면 1글자 씩임
#(W|w)ant(s)|(ed)|(ing)? -> ?을 마지막에 놔야 에러가 안날듯.
d = "Want want wnats wanted wnating"
m = p.findall(d) #findall로 안찾아짐_ 왜??
#왜 안찾아지냐면 : ()는 묶어주는 기능 & capture하는기능이 있음.
#그래서 ()하고 findall을 하면, ( ~ )를 찾아 가 아니라 "()"만!! 찾아~ 가 됨. 캡쳐돼서.
#그래서 search를 써야함 이럴때는.
print(m)

#text안에서 cat을 찾고 싶다면?
p = re.compile(r"[Cc]ats{0,1}") #개수를 조절하고 싶을 때 이렇게 쓰면 되겠지..???
p = re.compile(r"C|cats{0,1}") #둘다 가능
st = ["cat", "Cat", "Cats"]

for s in st:
    m = p.search(s)
    if m:
        print(s, "YES")
    else:
        print(s, "NO")
        
#14
p = re.compile("^[Ll]ife")
string = ["Life is short", "How short Life is"]
for s in string:
    m = p.search(s)
    if m:
        print(s, "YES")
    else:
        print(s, "NO")
        
#short
p = re.compile("short$")
string = ["Life is gggshort", "How short Life is"] #gggshort가 마지막에 있어도 YES로 나옴_단어가 아니라 진짜 마지막.

for s in string:
    m = p.search(s)
    if m:
        print(s, "YES")
    else:
        print(s, "NO")

#15p_match() -> match 객체를 돌려줌, 안되면 None
#"문자열의 처음부터" 정규식과 match 첫문자열 매치 안되면 None
p = re.compile("[a-z]+")
m = p.match("python") #<re.Match object; span=(0, 6), match='python'>
print(m)
m = p.match("3 python") #None
print(m) #None은 m.group해서 안뽑힘..
m = p.match("python 3") #<re.Match object; span=(0, 6), match='python'>
print(m)

#match 객체 말고 에쁘게 뽑고 싶으면 -> group()
print(m.group())

#findall
p = re.compile("[a-z]+")
result = p.findall("life is too short")
print(result) #string list return

#finditer()
result = p.finditer("life is too short")
print(result)

for r in result: 
    print(r)
    
#23
s1 = re.compile("a.b")
print(s1.match("a\nb"))

s1 = re.compile("a.b", re.S)
print(s1.match("a\nb"))

s1 = re.compile("a.b", re.DOTALL)
print(s1.match("a\nb"))

i = re.compile("cats?", re.I)
print(i.match("caTS"))

#multiline
m1 = re.compile("^python\s[a-z]+") #\s는 space
m2 = re.compile("^python\s[a-z]+", re.M) #['python one', 'python two', ~]
#이렇게 매 라인마다 python 들어있는 애 list로 반환

lines = """python one
python two
python three
python four"""

print(m1.findall(lines))
print(m2.findall(lines))

#\a, \Z 안중요해 버려
#ignorecase는 꼭 알아야 해 (나머진 버리라곤 못하지만)

#\b
b = re.compile(r"\bone\B") #\b one 이랑 다름
one1 = "python one python one python"
one2 = "python one onepython"
print(b.findall(one1))
print(b.findall(one2))

#\B
b = re.compile(r"\Bone\b") #one으로 끝나는 단어
#r : raw string이다 라는 데코레이터같은 것임. 있어야 원하는 대로 나옴
one1 = "python one python one python"
one2 = "python one one_python"
print(b.findall(one1))
print(b.findall(one2))

#문자열 치환 26p
data = "abc-def" #ab1-2de 가 있어도 문자 사이만 하고 싶어
data1 = re.sub("-", "#", data)
#-를 [a-z]-[a-z] 로 하면 안됨(뒤에서 배울 것임)
print(data1)

#re.subn : 몇번 치환했는지 튜플로 숫자 보여줌 _ 별로 안중요함. 버려

#정규표현식 심화2_2p
print(re.search("(abc)+" ,"abcabcabc")) #abcabcabc
print(re.search("(abc)|(def)", "_def_")) #def

m = re.search("00 [0=9]+ [0-9]+", "00 10 295")
print(m.group()) #00 10 295 _ 왜 None뜨지?
m = re.search("00 ([0=9]+) ([0-9]+)", "00 10 295")
#이렇게 괄호로 묶고 나면
print(m.group(1)) #10만 나옴_ 1번째 괄호만 보겠다
#만약 10 자리에 aa가 들어있고
print(m.group(2)) #이걸 하면 에러가 남. None인데 group 씌웠으니까.
#group(1) 부터는 ()로 안씌워져 있는건 반환 안해줌
#group(0)은 group()이랑 똑같음

#치환 + 삽입
p = re.compile(r"([a-zA-Z]+) ([0-9]+)[-]([0-9]+)[-]([0-9]+)")
re.sub(p, r"\1 : \2#\3#\4#", "Lee 010-1234-5678")

print(re.match("(12)+", "121212"))
print(re.search("(12)+", "121212"))
print(re.findall("(12)+", "121212")) #12 : 괄호를 같이 써서.. cature
print(re.fullmatch("(12)+", "121212")) #121212 다 나옴
#match는 처음부터 일치되어야 하는데, fullmatch는 처음부터 끝까지! 전부 일치해야 함.
print(re.fullmatch("(12)+", "0121212")) #None _ initial 떄문이 아니라, 전체가 일치되어야 하기 때문에.

#Examples with ()