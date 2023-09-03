from Prime import IsPrime
import math
n, m = map(int,input().split())
c = n
##def IsPrime(x):
##    for i in range(2, int(math.sqrt(x))+1):
##        if x % i == 0:
##            return False
##    return True
if IsPrime(m):
    while True:
        c += 1
        if IsPrime(c):
            if c == m:
                print("YES")
                break
            else:
                print("NO")
                break
else:
    print("NO")