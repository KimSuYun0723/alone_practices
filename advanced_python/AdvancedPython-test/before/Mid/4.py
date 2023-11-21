#!/usr/bin/env python3

import operator

print("---4번 문제---")

data = """Name: Kim Minju
Age: 22
Student_id: 20211020
Location: Seoul, South Korea
Phone: 010-1234-5678

Name: Lee Jihyun
Age: 20
Student_id: 20222021
Location: Busan, South Korea
Phone: 010-9876-5432

Name: Park Hyunwoo
Age: 25
Student_id: 20201022
Location: Incheon, South Korea
Phone: 010-5555-5555

Name: Choi Soomin
Age: 21
Student_id: 20221023
Location: Gwangju, South Korea
Phone: 010-1111-2222

Name: Kang Jaewon
Age: 23
Student_id: 20211024
Location: Daegu, South Korea
Phone: 010-9999-8888"""

print("---4-1번 문제---")

print("---첫번째 방법---")

data_split = data.split("\n")
index = 0
while index < len(data_split):
	line = data_split[index]
	if "Name" in line:
		print(line)
	index += 1
	
print("---두번째 방법---")

data_split2 = data.split()
index = 0
while index < len(data_split2):
	if data_split2[index] == "Name:":
		print(data_split2[index] + " " + data_split2[index + 1] + " " + data_split2[index + 2])
	index += 1
	
print("---4-2번 문제---")

age = {}
data_split3 = data.split("\n")
index = 0
while index < len(data_split3):
	line = data_split3[index]
	if "Name" in line:
		name = line[6:]
	if "Age" in line:
		age[name] = line[5:]
	index += 1
	
print(sorted(age.items(), key=lambda x: x[1], reverse=True))

print("---4-3번 문제---")

data_split4 = data.split("\n\n")
index = 0
while index < len(data_split4):
	student = data_split4[index]
	list = student.split("\n")
	studentName = list[0]
	studentId = list[2]
	if studentId[14:16] == "21":
		print(studentName[6:])
	index += 1
	