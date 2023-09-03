import math
a,b,s = (int(i) for i in input().split())
while(True):
    k = math.gcd(a,s)
    s-=k
    if (s==0):
        print(0)
        exit(0)
    elif (s<0):
        print(1)
        exit(0)
    k = math.gcd(b,s)
    s-=k
    if (s==0):
        print(1)
        exit(0)
    elif (s<0):
        print(0)
        exit(0)