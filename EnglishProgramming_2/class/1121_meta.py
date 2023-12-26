import re
p = re.compile("a.c")

string = ["(1) dfsfabc", "(2) abc", "(3) adc", "(4) alc", "(5) a\nc"]

for s in string:
    m = p.search(s)
    if m:
        print(s, "YES")
    else:
        print(s, "NO")

p = re.compile(".ing")

string = ["(1) running", "(2) jumping", "(3) singing", "(4) swimmng"]

for s in string:
    m = p.search(s)
    if m:
        print(s, "YES")
    else:
        print(s, "NO")