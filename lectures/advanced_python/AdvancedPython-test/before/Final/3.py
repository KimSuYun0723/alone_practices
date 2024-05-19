#!/usr/bin/env python3

print("~~~~~3번문제~~~~~")

f1 = open("salary.txt", "r")
data = f1.read()
f1.close()

data_list = data.split("\n")

levels = {}
num = {}
for i in range(1, len(data_list)):
	items = data_list[i].split("\t")
	
	level = items[2]
	salary = items[5]
	
	if level in levels:
		levels[level] += int(salary)
		num[level] += 1
	else:
		levels[level] = int(salary)
		num[level] = 1

levels_list = list(levels.keys())

for i in levels_list:
	level = i.replace("'s", "")
	sum = levels[i]
	n = num[i]
	print(f"{level}: ${sum/n}")