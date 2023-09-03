import sys
import math

a, b = [int(x) for x in (sys.stdin.readline()).split()]

n = 70
k = [True] * n

for i in range(2, int(math.sqrt(n))):
    if(k[i]):
        for j in range(i ** 2, n, i):
            k[j] = False

if(not k[b]):
    print("NO")
    exit()

for i in range(a + 1, b):
    if(k[i]):
        print("NO")
        exit()


print("YES")