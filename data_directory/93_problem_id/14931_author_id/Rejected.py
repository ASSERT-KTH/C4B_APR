k, a, b = map(int, input().split())
if a % k and b % k:
    print((b - a) // k)
else:
    print(1 + (b - a) // k)