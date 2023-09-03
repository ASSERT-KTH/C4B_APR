n, m, k = map(int, input().split())

ans = 0
base = 1e9 + 7
base = int(base)

if (k > n or k == 1) :
	ans = 1
	for i in range(n) :
		ans = ans * m % base
	print(ans)
elif (n == k) :
	ans = 1
	for i in range((n + 1) // 2) :
		ans = ans * m % base
	print(ans)
elif (n > k) :
	ans = m
	if (k % 2 == 1) :
		ans += m * (m - 1) // 2
	print(ans)