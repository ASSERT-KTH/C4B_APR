from sys import stdin

l,r,k= map(int,stdin.readline().split())
res = 1
p=0
if(l == 1):
    print(1,"",end='')
while(res <= r):   
    res *= k
    if(l <= res <= r):
        print(res,"",end='')
        p = 1
if(p == 0):
    print("-1")