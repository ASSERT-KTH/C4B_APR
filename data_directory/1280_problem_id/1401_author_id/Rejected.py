K = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
now = 0
for a in A:
    if now >= K:
        break
    now += a
    ans += 1
print(ans)