import re
p = re.compile("like.*")
string = ["like", "likely", "likelihood"]

for s in string:
    m = p.search(s)
    #m은 매치된 단어만 알려주는게 아니라 다양한 정보를 다알려주는 아이임.
    if m:
        print(s, "YES")
    else:
        print(s, "NO")
        
p = re.compile("ca+t")
string = ["cat", "caat", "caaaaat"]

p = re.compile("[A-Z]+")
string = ["CAT", "Caat", "caaaaat"]

p = re.compile("ca{2}t")
string = ["CAT", "caat", "caaaaat"]

p = re.compile("ab?c")
string = ["abc", "ac"]

p = re.compile("a|b")
string = ["abcd", "ac"]

for s in string:
    m = p.search(s)
    #m은 매치된 단어만 알려주는게 아니라 다양한 정보를 다알려주는 아이임.
    if m:
        print(s, "YES")
    else:
        print(s, "NO")