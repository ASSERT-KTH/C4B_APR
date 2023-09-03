a, b = map(int, input().split())
c, d = map(int, input().split())
x1 = (b + a * 1) % 2 == 0
x2 = (b + a * 2) % 2 == 0
x3 = (d + c * 1) % 2 == 0
x4 = (d + c * 2) % 2 == 0
if (x1 == x2) and (x3 == x4) and (x1 != x3):
	print(-1)
else:
	ans = b + a
	while(True):
		if (ans - d) % c == 0:
			print(ans)
			exit(0)
		ans += a