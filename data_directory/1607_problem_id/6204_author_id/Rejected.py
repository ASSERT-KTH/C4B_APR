import math
l, r = map(int, input().split())
ans = (l <= 9) * (min(r, 9) - l + 1)
for k in range(0, 17):
  for d in range(1, 10):
    rb = math.floor((r - d - 10 ** (k + 1) * d) / 10)
    lb = math.ceil((l - d - 10 ** (k + 1) * d) / 10)
    rx = min(10 ** k - 1, rb)
    lx = max(0, lb)
    ans += (rx >= lx) * (rx - lx + 1)
print(ans)