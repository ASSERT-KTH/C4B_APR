n, m = map(int, input().split())
x, v = int(input()), 0
x1, y1, x2, y2 = x - 1, x - 1, n - x, m - x
if x1 > x2 or y1 > y2:
    print(0)
    exit()
for i in range(x1, x2 + 1):
    if i == x1 or i == x2:
        v += (y2 - y1 + 1) // 2 + ((i + y1) % 2 == 0 and (i + y2) % 2 == 0)
    else:
        v += ((i + y1) % 2 == 0) + ((i + y2) % 2 == 0)
print(v)