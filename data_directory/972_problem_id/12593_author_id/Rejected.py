l, r = list(map(int, input().split()))
if r == 0:
	print('NO')
else:
	print('YES' if abs(l - r) <= 1 else 'NO')