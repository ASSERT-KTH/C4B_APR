a, b = (int(i) for i in input().split())
t = 0
if a > b:
    a, b = b, a
if b < 2:
    print(0)
else:
    while b > 2:
        x = (b - 1) // 2
        t += x
        a += x
        b -= 2 * x
        a, b = b, a
    print(t + 1)