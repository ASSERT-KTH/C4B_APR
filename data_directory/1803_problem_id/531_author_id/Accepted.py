'''input
508
'''
from math import gcd
n, m = int(input()), 0
if n <= 3:
	print([1, 2, 6][n-1])
elif n % 2 == 1:
	print(n*(n-1)*(n-2))
elif n % 3 == 0:
	print((n-1)*(n-2)*(n-3))
else:
	print(n*(n-1)*(n-3))