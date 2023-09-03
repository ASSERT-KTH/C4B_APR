#!/bin/python3

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k == 1 or l == 1 or m == 1 or n == 1:
	print(d)
else:
	a = [int(x) for x in range(k, d+1, k)]
	b = [int(x) for x in range(l, d+1, l)]
	c = [int(x) for x in range(m, d+1, m)]
	d = [int(x) for x in range(n, d+1, n)]
	
	print(len(set(a+b+c+d)))