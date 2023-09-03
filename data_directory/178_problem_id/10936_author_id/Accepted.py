from sys import stdin

l,r,k= map(int,stdin.readline().split())
res = 1
p = 0
get = 0
while(res <= r): 
    if(l == 1 and get == 0):
        print(1,"",end='')
        get = 1
        p = 1
    res *= k
    if(l <= res <= r):
        print(res,"",end='')
        p = 1
if(p == 0):
    print("-1")