import math
a, b, n = map(int, input().split())
while(True):
    if(n == 0):
        print("1")
        break
    n -= math.gcd(a, n)
    if(n == 0):
        print("0")
        break
    n -= math.gcd(a, n)