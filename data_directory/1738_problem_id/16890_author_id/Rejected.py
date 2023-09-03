from math import gcd
a,b,c=map(int,input().split())
a = gcd(a,b)
b//=a
c = gcd(a,c)
print(a*4+b*4+c*4)