x, y = map(int, input().split())
a, v = [y] * 3, 0
while a[0] < x:
    a[0] = min(x, a[1] + a[2] - 1)
    a.sort()
    v += 1
print(v)