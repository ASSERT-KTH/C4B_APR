n, k = input().split(' ')
k = int(k)
cur = 0
ans = 0
great = False
for c in reversed(n):
    if cur >= k:
        great = True
        break
    if c == '0':
        cur += 1
    else:
        ans += 1
if great:
    print(ans)
else:
    print(len(n) - 1)