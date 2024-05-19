#!/usr/bin/env python3

print("~~~~~1-1번문제~~~~~")

def mycount(a, b):
	result = 0
	for i in a:
		if i == b:
			result += 1
			
	print(result)
			
a = "abcabc"
b = ["a", "b", "c", "a", "b", "c"]

mycount(a, "a")
mycount(b, "a")


print("~~~~~1-2번문제~~~~~")

def myset(a):
	result = []
	for i in a:
		if i not in result:
			result.append(i)
			
	return result

b = ["a", "b", "c", "a", "b", "c"]

print(myset(b))

