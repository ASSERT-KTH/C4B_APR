x, y = list(map(int, input().split()))
a = True
d = 1
while a:
    n = x * 3
    m = y * 2

    if n > m:
        print(d)
        a = False

    elif m >= n:
        d += 1
        x = n
        y = m