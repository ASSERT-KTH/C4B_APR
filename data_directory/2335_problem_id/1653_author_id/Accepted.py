#!/bin/python3

import string

greetings = 'hello'

s = [x for x in input() if x in greetings]
j = 0
temp = ''

for x in greetings:
	
	if x in s:
		s = s[s.index(x):]
	else:
		print('NO')
		break
	
	if x == s[0]:
		temp += x
		s = s[1:]

	if temp == greetings:
		print('YES')
		break