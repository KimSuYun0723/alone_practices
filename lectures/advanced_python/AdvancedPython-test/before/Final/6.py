#!/usr/bin/env python3

print("~~~~~6번문제~~~~~")

def salary(file, career1=-1, career2=-1):
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
		
		if (career1 == career2 == -1) or (career2 == -1 and int(years) <= career1) or (career1 <= int(years) <= career2):
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
			


print("~~~~~5년 이하 사람들의 평균 연봉을 구하는 경우~~~~~")
salary("salary.txt", 5)

print("~~~~~5년 이상 10년 이하인 사람들의 평균 연봉을 구하는 경우~~~~~")
salary("salary.txt", 5, 10)

print("~~~~~경력 기간을 입력하지 않은 경우~~~~~")
salary("salary.txt")