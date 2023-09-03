#! /usr/bin/python3

def solve():
	x, y, z = map(int, input().strip().split())
	a, b, c = map(int, input().strip().split())
	
	ret = 0
	if (x * b == y * a):
		if (y == 0 and b == 0):
			if c * x == a * z:
				ret = -1
			else:
				ret = 0
		elif z * b == y * c:
			ret = -1
		else:
			ret = 0
	else:
		ret = 1
	
	if (x == y and y == a and a == b and b == 0):
		if (z == c):
			ret = -1
		else:
			ret = 0
	print(ret)

solve()