import math

n, m, a = [int(x) for x in input().split()]
r = math.ceil(n / a)
c = math.ceil(m / a)

print(r * c)