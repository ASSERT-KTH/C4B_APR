'''input
1
'''
from math import floor
n = int(input())
if n == 1:
	print(0, 1)
elif n % 7 == 0:
	print(2*n//7, 2*n//7)
elif n % 7 <= 5:
	print(n//7*2, n//7*2 + 2)
else:
	print(n//7*2 + 1, n//7*2 + 2)