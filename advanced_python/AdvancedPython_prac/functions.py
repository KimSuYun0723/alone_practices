    #round(반올림할 값, 반올림자릿수) : 
"""
- 자릿수 입력 안하면 정수형으로
- 반올림_n자리 "까지" 반올림
>>> 
3.0 ==> 자료형이 다름
"""
a = round(3.141592, 0) 
print(a, type(a)) #float

b = round(3.141592)
print(b, type(b)) #int

    #abs()_무리수 포함 모든 실수 가능
a = -2**(1/2)
print(abs(-a))

    #slicing
s = "abcdefghi"
print(s[:3])
print(s[::])
print(s[::2])
print(s[:-4])
print(s[-4:])

    #text.replace(old,new,개수)

    #lower(),upper()