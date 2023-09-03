import math

n, a, b, c = [int(x) for x in input().split(" ")]


f = [0]*(n+1)

f[0] = 0

for i in range(1,n+1):
	x = f[i-a]
	y = f[i-b]
	z = f[i-c]
	if i-a < 0:
		x = -math.inf
	if i-b < 0:
		y = -math.inf
	if i-c < 0:
		z = -math.inf
	f[i] = max(1 + x, 1 + y, 1 + z)
print(f[n])