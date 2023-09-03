#!/bin/python3

import string

greetings = 'hello'

s = [x for x in input() if x in greetings]
j = 0
temp = ''

for x in greetings:
	
	while(x != s[0])and(len(s)>1):
		s = s[1:]
	
	if x == s[0]:
		temp += x
		s = s[1:]

	if temp == greetings:
		break
	
if temp == greetings:
	print('YES')
else:
	print('NO')