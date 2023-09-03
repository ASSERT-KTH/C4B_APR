from math import gcd

a,b,c=tuple(input().split(" "))
a=int(a)
b=int(b)
c=int(c)
while True:
    if gcd(a,c)>c:
        print("1")
        exit(0)
    c-=gcd(a,c)
    if gcd(b,c)>c:
        print("0")
        exit(0)
    c-=gcd(b,c)