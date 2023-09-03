a, b = map(int, input().split())
c , d = map(int, input().split())

for i in range(0,101):
	j = ((a * i) + b - d) / c
	if  j == int(j) and j >= 0:
		print((a * i) + b)
		break
else: print(-1)