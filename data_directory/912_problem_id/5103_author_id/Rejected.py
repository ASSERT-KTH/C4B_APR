n, k = map(int, input().split())

ans = 0
while k + 5 * ans < 240:
	ans += 1
	k += 5 * ans
	if ans == n:
		break
print(ans)