n = (int)(input())

ans = 0
if (n%2 != 0):
	ans = 7
	n -= 3

while (n > 0):
	ans *= 10
	ans += 1
	n -= 2

print(ans)