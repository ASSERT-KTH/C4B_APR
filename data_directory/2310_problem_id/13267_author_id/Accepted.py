import sys
import math

n = int(sys.stdin.readline())

v = []

x = 1
y = n
for i in range(n):
    if(i % 2 == 0):
        v.append(str(x))
        x += 1
    else:
        v.append(str(y))
        y -= 1
    
print(" ".join(v))