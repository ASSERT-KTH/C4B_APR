n, m, a, b = map(int, input().split())


if (a - 1) // m == (b - 1) // m:
    print("1")
elif abs((a - 1) // m - (b - 1) // m) == 1 and a % m != 1:
    print("2")
elif b == n or b % m == 0:
    if a % m == 1:
        print("1")
    else:
        print("2")
elif a % m == 1 or ((b + (m - a % m + 1)) % m) == 0:
    print("2")
else:
    print("3")