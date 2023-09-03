'''input
6 11 6
'''
from math import gcd
a, b, c = map(int, input().split())
for x in range(c//a+1):
	if (c - x*a) % b == 0:
		print("Yes")
		break
else:
	print("No")