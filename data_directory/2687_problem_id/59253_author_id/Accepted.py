from math import *

n,m = [int(j) for j in input().split()]

if n <= m:
    print(n)
else:
    k= ceil((-1 + sqrt(1 + 8*(n-m)))/2)
    while (k*(k+1) >= 2 * (n - m)):
        k -= 1
    k += 1
    print(m + k)