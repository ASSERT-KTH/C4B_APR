from math import *
a, b = input().split()
c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = abs(a-c)
f = abs(b-d)
g = 0
if e >= f:
	print(e)
elif f >= e:
	print(f)	

# 1481129670451