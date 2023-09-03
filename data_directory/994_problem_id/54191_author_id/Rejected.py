n, m, a = [int(x) for x in input().split()]
r = int(n / a + 0.5)
c = int(m / a + 0.5)

print(r * c if r * c > 0 else 1)