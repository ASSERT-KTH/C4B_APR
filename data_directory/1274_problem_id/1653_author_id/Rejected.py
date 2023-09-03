#!/bin/python3

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k == 1 or l == 1 or m == 1 or n == 1:
	print(d)
else:
	tab = []
	
	temp = k
	while k <= d:
		if k not in tab:
			tab.append(k)
		k += temp
	temp = l
	while l <= d:
		if l not in tab:
			tab.append(l)
		l += temp
	temp = m
	while m <= d:
		if m not in tab:
			tab.append(m)
		m += temp
	temp = n
	while n <= d:
		if n not in tab:
			tab.append(n)
		n += temp
	
	print(len(tab))