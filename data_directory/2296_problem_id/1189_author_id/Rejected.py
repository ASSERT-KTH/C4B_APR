m, n = [int(x) for x in input().split()]

a = m * (n // 2) + m // 2 * (m % 2)
b = n * (m // 2) + n // 2 * (n % 2)
print(max(a, b))