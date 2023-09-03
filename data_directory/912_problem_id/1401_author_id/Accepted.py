N, K = map(int, input().split())
rem = 240 - K

cnt = 5
acc = 0
ans = 0

while acc < rem:
    if acc + cnt <= rem:
        acc += cnt
        ans += 1
        cnt = 5 * (ans + 1)
    else:
        break
print(min(N, ans))