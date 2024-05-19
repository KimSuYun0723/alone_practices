#!/usr/bin/env python3

import mydef

print("~~~~~2-1번문제~~~~~")

f1 = open("oliver.txt", "r")
data = f1.read()
f1.close()

data = data.replace(",", "").replace(".", "").lower()
data_list = data.split()
result = mydef.mycount(data_list, "he")

print(f"The frequency of the word 'he' is {result}")


print("~~~~~2-2번문제~~~~~")

f2 = open("oliver.txt", "r")
data = f2.read()
f2.close()

data = data.replace(",", "").replace(".", "").lower()
data_list = data.split()

data_unique = mydef.myset(data_list)

f3 = open("word_list.txt", "w")
f3.write("#2-2)번문제# 202003099 전효원\n")

for i in range(len(data_unique)):
	f3.write(f"{i+1}. {data_unique[i]}\n")
	
f3.close()