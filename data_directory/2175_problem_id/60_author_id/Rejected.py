import math
n,m,s = map(int, input().split())
c = 0
cc = 0
su = 0
ss = 0

if ((s >= m and s >= n) or s == 1 or (m%s==0 and n%s==0)):
    print(m*n)
else:
    su = (math.ceil(n/s) * math.ceil(m/s))
    print (su* (n%s) * (m%s))