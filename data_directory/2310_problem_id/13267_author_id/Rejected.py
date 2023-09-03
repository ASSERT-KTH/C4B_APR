import sys
import math

n = int(sys.stdin.readline())

p = [''] * (n + 1)

x = 1
y = n
for i in range(1, n + 1):
    if(i % 2 != 0):
        p[x] = str(i)
        x += 1
    else:
        p[y] = str(i)
        y -= 1
        
print(" ".join(p[1:]))