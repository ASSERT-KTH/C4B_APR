from math import ceil

n, m, a = [int(x) for x in input().split(' ')]

modifier = 0

if n == a or m == a:
    modifier = 1
    print(ceil(n / a) + ceil(m / a) - modifier)
elif a > n and a > m:
    print(1)
else:
    print(ceil(n / a) + ceil(m / a) - modifier)