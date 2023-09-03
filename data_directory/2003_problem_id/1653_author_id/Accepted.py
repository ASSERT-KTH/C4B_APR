#!/bin/python3

x = int(input())+1

while True:
	a = [str(y) for y in str(x)]
	if len(set(a)) == len(str(x)):
		print(x)
		break
	else:
		x += 1
		continue