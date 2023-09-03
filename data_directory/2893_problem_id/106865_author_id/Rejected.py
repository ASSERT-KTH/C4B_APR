import math
import time

st = input().split()
n = int(st[0])
k = int(st[1])

a = n // (2 * k + 2)
if a != 0:
   b = (k * n) // (2 * k + 2)
   c = n - a - b
else:
   b = 0
   c = n
print(a, b, c)