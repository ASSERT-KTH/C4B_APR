n, a, b, c = map(int, input().split())
count = 0
for ci in range(c + 1):
  x = n - 2 * ci
  if x < 0:
    break
  for bi in range(b + 1):
    y = x - bi
    if y < 0:
      break
    if 2 * y <= a:
      count += 1

print(count)