n, a, b, c = map(int, input().split())
lengths = {a, b, c}
dp = [0] * n

for i in range(n):
    options = [0]
    for l in lengths:
        if i - l >= 0:
            options.append(dp[i - l] + 1)
    dp[i] = max(options)

print(dp[-1])