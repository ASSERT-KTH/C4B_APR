n, m, k = map(int, input().split())

def check(l, r) :
	while (l < r) :
		if (s[l] != s[r]) :
			return False
		l += 1
		r -= 1
	return True

s = [0] * n

def rec(v) :
	if (v == n) :
		for i in range(n - k + 1) :
			if (not check(i, i + k - 1)) :
				return ;
		res = ''
		for i in range(n) :
			res = res + str(s[i]) + ' '
		print(res)
	else :
		for i in range(m) :
			s[v] = i
			rec(v + 1)  	


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
		ans += m * (m - 1)
	print(ans % base)