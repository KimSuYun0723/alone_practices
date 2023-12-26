import re
p = re.compile(r"([a-zA-Z]+) ([0-9]+)[-]([0-9]+)[-]([0-9]+)")
a = re.sub(p, r"\1 \2#\3#\4#", "Lee 010-1234-5678")
print(a)

data = "good morning, mr. smith. how are you? i'm fine, thank you. how's the weather outside? it's rainy today."
p = re.compile(r"(.*) (mr.) (.*)")
a = re.sub(p, r"\1 \2# \3" ,data)
print(a)

print(re.findall('\d{4}-(\d\d)-(\d\d)', '1999/05/21 2018-07-28 2018-06-31 2019.01.01'))

data = "Good morning, Mr. Smith. How are you? I’m fine, thank you. How’s the weather outside? It’s rainy today."
re.split(r"\.|\?", data)

p = re.compile(r"\w+(?=:)")
script = "Joey: Instead of...?"
m = p.findall(script)
print(m)

p = re.compile(r"(?<=: ).+")
script = "Joey: Instead of...?"
m = p.findall(script)
print(m)

d1 = """I paid 30000won for 100 apples,
50 oranges, and 60 pears.
I saved 5000won on this order."""
d2 = """I paid $30 for 100 apples,
50 oranges, and 60 pears.
I saved $5 on this order."""

p= re.compile(r"\b\d+\b(?!won)")
m = p.findall(d1)
print(m)

p= re.compile(r"\b(?<!\$)\d+\b")
m = p.findall(d2)
print(m)

########################################################
#문장 나누기
data = "Good morning, Mr. Smith. How are you? I'm fine, thank you. How's the weather outside? It's rainy today."
p1 = re.compile(r"(?<=[A-Z][a-z])\.")
print(p1.findall(data))
data = re.sub(p1, "&", data)
print(data) #Mr. --> Mr&

new_d = ""
p = re.compile(r"\.|\?")
for d in data:
    if p.search(d):
        new_d += d+"\n"
        print(new_d)
    else:
        new_d += d
        print(new_d)

sen = new_d.split("\n")[:-1]
sen[0] = re.sub("&", ".", sen[0])
print(sen)