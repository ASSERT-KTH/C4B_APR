'''input
2 4 5
'''
l, r, k = map(int, input().split())
t = 0
for x in range(100000):
	if k**x >= l and k**x <= r:
		print(k**x, end=" ")
		t = 1
	elif k**x > r:
		break
if t == 0:
	print(-1)