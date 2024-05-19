#!/usr/bin/env python3

print("~~~~~4번문제~~~~~")

def salary(file, career):
	f1 = open(file, "r")
	data = f1.read()
	f1.close()
	
	data_list = data.split("\n")
	
	levels = {}
	num = {}
	for i in range(1, len(data_list)):
		items = data_list[i].split("\t")
		
		level = items[2]
		salary = items[5]
		years = items[4]
		
		if int(years) <= career:
			if level in levels:
				levels[level] += int(salary)
				num[level] += 1
			else:
				levels[level] = int(salary)
				num[level] = 1
		else:
			if level in levels:
				pass
			else:
				levels[level] = 0
				num[level] = 0
				
	levels_list = list(levels.keys())
		
	for i in levels_list:
		level = i.replace("'s", "")
		sum = levels[i]
		n = num[i]
		if n == 0:
			print(f"{level}: $0")
		else:
			print(f"{level}: ${round(sum/n)}")
		
salary("salary.txt", 5)