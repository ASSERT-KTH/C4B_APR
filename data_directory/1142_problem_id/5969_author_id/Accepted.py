n, a, b = list(map(int, input().split()))
if (n - a) < (b + 1):
    print(n - a)
else:
    print(b + 1)