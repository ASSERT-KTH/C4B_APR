'''input
1 999999999999999999 1000000000
'''
l, r, k = map(int, input().split())
for x in range(100000):
	if k**x >= l and k**x <= r:
		print(k**x, end=" ")
	elif k**x > r:
		break
else:
	print(-1)