k, b, n, t = map(int, input().split())
if t == 1:
    print(n)
elif k == 1:
    print(max(0, (n * b - t + b - 1) // b))
else:
    x, y, v = k - 1 + b, t * (k - 1) + b, 0
    while x <= y:
        x *= k
        v += 1
    print(max(0, n - v + 1))