m, n = map(int, input().split())

if m == 1 and n % 2 == 0:
    print(int(n / 2))
elif m % 2 == 0 and n == 1:
    print(int(m / 2))
elif m % 2 == 0 or n % 2 == 0:
    print(int((m * n) / 2))
elif m % 2 != 0 and n % 2 != 0:
    print(int(((m * n) - 1) / 2))