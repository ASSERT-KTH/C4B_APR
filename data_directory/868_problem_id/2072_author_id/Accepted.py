n = int(input())
if n == 0:
    print(1)
else:
    n %= 4
    res = 6
    for i in range(1, n + 1):
        res *= 8
    print(res % 10)