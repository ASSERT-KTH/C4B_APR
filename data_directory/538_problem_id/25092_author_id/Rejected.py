from collections import Counter

t = list(map(int, input().split(' ')))
cnt = Counter()
for tt in t:
    cnt[tt] += 1
ans = sum(t)
for tt, n in cnt.items():
    if n == 2 or n == 3:
        ans = min(ans, sum(t) - n * tt)
print(ans)