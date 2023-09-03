I = lambda: int(input())
n, a, b, c = I(), I(), I(), I()
m = max(n // a, ((n - b) // (b - c) + 1) if b <= n else 0)
print(m + max(0, n - m * (b - c)) // a)