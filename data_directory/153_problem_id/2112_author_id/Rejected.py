n = int(input())
if (n % 2):
	print(0)
else:
	ans = 0
	n //= 2
	for i in range(1, n // 2 + 1):
		if(i < n - i):
			ans += 1
	print(ans)