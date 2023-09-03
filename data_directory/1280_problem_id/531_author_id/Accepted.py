'''input
0
0 0 0 0 0 0 0 1 1 2 3 0
'''
k = int(input())
a = list(map(int, input().split()))
if sum(a) < k:
	print(-1)
elif k == 0:
	print(0)
else:
	s, t = 0, 0
	a = sorted(a)[::-1]
	while s < k:
		s += a[0]
		t += 1
		del a[0]
	print(t)