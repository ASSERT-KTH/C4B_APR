from math import sqrt
from math import ceil
n,m = map(int, input().split())
barn = n
if n <= m:
	print(n)
else:
	days = ceil((-1 + float(sqrt(1+8*(n-m))))/2)
	print(days + m)