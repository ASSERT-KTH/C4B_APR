n, a, b, c = map(int, input().split())
print([0, min(3*a, a+b, c), min(2*a, b, 2*c), min(a, b+c, 3*c)][n % 4])