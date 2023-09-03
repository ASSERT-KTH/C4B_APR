n, m, a, b = map(int, input().split())
if b == n:
    b += m - 1 - (b - 1) % m
c1, c2 = (a - 1) % m, (b - 1) % m
if (a - 1) // m == (b - 1) // m or c1 == 0 and c2 == m - 1:
    print(1)
elif c1 == 0 or c2 == m - 1 or c1 == c2 + 1:
    print(2)
else:
    print(3)