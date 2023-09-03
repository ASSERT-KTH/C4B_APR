from math import *

n,k = map(int,input().split(" "))

if n == 1:
    print(0)
    exit(0)
if k+1 == n:
    print(2)
    exit(0)
    
if k >= n:
    print(1)
    exit(0)

d = (2*k-3) ** 2 + 8*(k-n)


if d < 0:
    print(-1)
    exit(0)
    
if d == 0:
    x1 = (2 * k - 3) / 2
    if x1 < 0 or ceil(x1) > k-2:
        print(-1)
    else:
        if (x1 == ceil(x1)):
            print(x1+2)
        else:
            print(ceil(x1)+1)
    exit(0)

x1 = ((2 * k - 3) - sqrt(d)) / 2 
x2 = ((2 * k - 3) + sqrt(d)) / 2

if x1 <= 0:
    if x2 <= 0 or ceil(x2) > k-2:
        print(-1)
    else:
        if (x1 == ceil(x1)):
            print(x1+2)
        else:
            print(ceil(x1)+1)
else:
    if x1 <= 0 or ceil(x1) > k-2:
        print(-1)
    else:
        print(ceil(x1)+1)