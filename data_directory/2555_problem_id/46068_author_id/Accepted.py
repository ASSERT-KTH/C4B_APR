#!/usr/bin/python
# -*- coding: UTF-8 -*-
team = list(input())
team = [int(i) for i in team]
counter = 0
index = 0
flag = False
for i in range(len(team)):
	if (counter >= 6 and team[i] == team[index]):
		flag = True
		break 
	if(team[index] == team[i]):
		counter += 1
	else:
		counter = 1
		index = i
if(flag):
	print("YES")
else:
	print("NO")