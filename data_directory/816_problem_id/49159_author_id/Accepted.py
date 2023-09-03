def solve(a, b, c):
	if a < 0 or b < 0 or c < 0:
		return 1e19
	if a == 0 and b == 0 and c == 0:
		return 0

	a = max(a, 0)
	b = max(b, 0)
	c = max(c, 0)

	d = min(a, b, c)
	a = a - d
	b = b - d
	c = c - d

	arr = [a, b, c]
	arr.sort()

	return arr[1] + (arr[2] - arr[1]) * 2

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

ans = 1e19
ans = min(ans, solve(a, b, c)) # 0 0
ans = min(ans, solve(a, b - 1, c)) # 0 0
ans = min(ans, solve(a - 1, b, c)) # 0 1
ans = min(ans, solve(a, b, c - 1)) # 1 0
ans = min(ans, solve(a - 1, b - 1, c)) # 0 2
ans = min(ans, solve(a - 1, b, c - 1)) # 1 1
ans = min(ans, solve(a, b - 1, c - 1)) # 2 0
ans = min(ans, solve(a - 1, b - 2, c - 1)) # 2 2

print(ans)