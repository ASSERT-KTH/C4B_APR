from math import *
n,m,s=map(int,input().split())
r = ceil(n/s) * (s if n%s==0 else n%s)
c = ceil(m/s) * (s if m%s==0 else m%s)
ans=r*c
print(ans)