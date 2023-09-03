n, k = map(int, input().split())
energy = sorted(list(map(int, input().split())))
factor = (100 - k) / 100

low = 0
high = sum(energy) / n
while high - low > 1e-6:
  mid = (low + high) / 2
  balance = 0
  for x in energy:
    if x > mid:
      balance -= factor * (x - mid)
    else:
      balance += mid - x
  if balance < 0:
    low = mid
  else:
    high = mid

print(high)