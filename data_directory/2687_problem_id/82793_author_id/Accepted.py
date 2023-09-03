from math import ceil
from decimal import Decimal
n,m = map(int, input().split())
barn = n
if n <= m:
	print(n)
else:
	days = ceil((-1 + Decimal(1+8*(n-m)) ** Decimal(0.5))/2)
	print(days + m)