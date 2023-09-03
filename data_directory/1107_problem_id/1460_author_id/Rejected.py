from math import gcd

a,b,c=tuple(input().split(" "))
a=int(a)
b=int(b)
c=int(c)
while c>a and c>b:
    c-=gcd(a,c)
    if c<a:
        break
    c-=gcd(b,c)
if c<a:
    print("1")
else:
    print(0)