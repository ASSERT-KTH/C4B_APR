n, k = input().split(' ')
k = int(k)
cur = 0
ans = 0
for c in reversed(n):
    if cur >= k:
        break
    if c == '0':
        cur += 1
    else:
        ans += 1
print(ans)