def baby_step_giant_step(a, b, m):
  n = int(m ** .5) + 1
  an = pow(a, n, m)
  vals = [0] * m
  cur = an
  for i in range(1, n + 1):
    if vals[cur] == 0:
      vals[cur] = i
    cur = cur * an % m

  cur = b
  for i in range(0, n + 1):
    if vals[cur] != 0:
      ans = vals[cur] * n - i
      if ans < m:
        return ans
    cur = cur * a % m
  return -1


mod = 10 ** 9 + 7
p, k = [int(x) for x in input().split()]
if k == 0:
    print(pow(p, p - 1, mod))
elif k == 1:
    print(pow(p, p, mod))
else:
    print(pow(p, (p - 1) // baby_step_giant_step(k, 1, p), mod))