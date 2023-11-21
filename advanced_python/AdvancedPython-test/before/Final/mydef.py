#!/usr/bin/env python3

def mycount(a, b):
	result = 0
	for i in a:
		if i == b:
			result += 1
			
	return result
	
def myset(a):
	result = []
	for i in a:
		if i not in result:
			result.append(i)
			
	return result
