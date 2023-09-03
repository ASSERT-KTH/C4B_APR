a, b = map(int, input().split())
if a >= b:
    print(a + b - 1 - (b | 1), (b | 1))
else:
    print((a | 1), a + b - 1 - (a | 1))