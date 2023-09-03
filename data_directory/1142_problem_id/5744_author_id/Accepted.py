n, a, b = map(int, input().split())
print(n - a if n - a <= b + 1 else b + 1)