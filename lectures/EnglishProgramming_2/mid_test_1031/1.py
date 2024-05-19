print("===============1번문제=================")
f = open("file_open.txt", "r", encoding="utf-16")
data = f.readlines()
data_2 = []
for i in data:
    print(i.rstrip("\n"))
f.close()