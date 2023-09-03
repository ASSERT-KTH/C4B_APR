import math
a,b,n = [int(i) for i in input().split()]
l = 0

while True:
    minus = math.gcd(a,n)
    
    if n > minus:
        n -= minus
        l = 1
    else:
        l = 0
        break

    minus = math.gcd(b,n)
    
    if n > minus:
        n -= minus
        l = 0
    else:
        l = 1
        break

print(l)
import math
a,b,n = [int(i) for i in input().split()]
l = 0

while True:
    minus = math.gcd(a,n)
    
    if n > minus:
        n -= minus
        l = 1
    else:
        l = 0
        break

    minus = math.gcd(b,n)
    
    if n > minus:
        n -= minus
        l = 0
    else:
        l = 1
        break

print(l)