'''input
581
196122941
'''
from math import log
k, l = int(input()), int(input())
if log(l, k) == float(log(l, k)):
	print("YES")
	print(int(log(l, k) - 1))
else:
	print("NO")