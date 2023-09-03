import sys

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

a, b, c = tuple(map(int, input().split()))

if b == c or a < min(b, c):
	print("1/1")
	sys.exit(0)

ans = min(b, c) - 1

x = b * c // gcd(b, c)

ans += ((a // x) * (min(b, c)))

y = max((a // x) * x + min(b, c) - 1 - a, 0)
ans -= y;
print(str(ans) + "/" + str(a))