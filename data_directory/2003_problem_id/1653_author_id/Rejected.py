#!/bin/python3

x = int(input())

for i in range(x+1, 9001):
	
	a = [str(y) for y in str(i)]

	if len(set(a)) == 4:
		print(i)
		break
	else:
		continue