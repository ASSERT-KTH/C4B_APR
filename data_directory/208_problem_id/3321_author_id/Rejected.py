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
if e == 0:
	print(f)
if f == 0:
	print(e)
else:
	if e == f:
		print(e)
	elif e > f:
		g = e-f
		print(f+g)
	elif f > e:
		g = f-e
		print(e+g)			

# 1481128837238