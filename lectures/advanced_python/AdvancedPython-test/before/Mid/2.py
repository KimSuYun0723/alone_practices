#!/usr/bin/env python3

print("---2번 문제---")

i = 2
j = 2

while i <= 4:
	while j <= 4:
		print("{0}의 {1}제곱: {2}".format(i, j, i**j))
		j += 1
	i += 1
	j = 2