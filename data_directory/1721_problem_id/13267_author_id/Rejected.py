import sys
import math

n = int(sys.stdin.readline())

a = []

for i in range(n, 0, -1):
    a.append(str(i))
    
print(" ".join(a))