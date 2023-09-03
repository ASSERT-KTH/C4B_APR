import sys
import math
  
n, k = [int(x) for x in (sys.stdin.readline()).split()]

if(k == 1 and n == 1):
    print("a")
    exit()

if(k == 1 or k > n):
    print(-1)
    exit()

t = 2
for i in range(n):
    if(n - (k - 2) > i):
        if(i % 2 == 0):
            sys.stdout.write('a')
        else:
            sys.stdout.write('b')
    else:
        sys.stdout.write(chr(t + 97))
        t += 1