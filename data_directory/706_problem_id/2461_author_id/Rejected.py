x, y = map(int, input().split())
a, v = [x] * 3, 0
while a[2] > y:
    a[2] = max(a[1] - a[0] + 1, y)
    a.sort()
    v += 1
print(v)