n = int(input())
for y in range(n + 1, 10000):
  d1, d2, d3, d4 = y // 1000, (y // 100) % 10, (y // 10) % 10, y % 10
  if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
    print(y)
    break