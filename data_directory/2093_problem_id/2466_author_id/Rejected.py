from string import ascii_lowercase
n, k = [int(x) for x in input().split()]
if n < k or k == 1:
	print(-1)
	exit(0)
print('ab' * ((n - k + 2) // 2) + ('a' if (n + k) % 2 == 1 else '') + ascii_lowercase[2: k])