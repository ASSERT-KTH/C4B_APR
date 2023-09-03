n = int(input())
ans = 0
if n % 2 == 0:
  for i in range(0, n // 4 - 1):
    ans += 1
  if n % 4 == 0:
    ans -= 1
print(ans)