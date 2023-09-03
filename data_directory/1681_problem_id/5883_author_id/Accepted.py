import math
n,m = map(int, input().split())
a = 0
c = 0
while(a<=m):
    t = (n - a*a)
    v = math.sqrt(m-a)
    if(t == v):
        c+=1
    a = a+1
print(c)