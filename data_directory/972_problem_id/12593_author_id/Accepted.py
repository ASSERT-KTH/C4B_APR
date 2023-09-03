l, r = list(map(int, input().split()))
if l == r and l == 0:
	print('NO')
else:
	print('YES' if abs(l - r) <= 1 else 'NO')