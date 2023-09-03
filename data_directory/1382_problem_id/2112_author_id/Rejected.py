MOD = 10 ** 9 + 7

n = int(input())

dp = [[0] * 4 for _ in range(n + 1)]

dp[0][0] = 1

for i in range(n):
	for j in range(4):
		for k in range(4):
			if j != k:
				dp[i+1][j] = (dp[i][k] + dp[i+1][j]) % MOD

print(dp[n][0])