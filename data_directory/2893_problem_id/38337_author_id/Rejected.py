n,k=map(int,input().split())
half=n//2
d=0
c=0
u=0
i=half
while i>=0:
    if i%(k+1)==0:
        d=i//(k+1)
        c=i-d
        u=n-i
        break
    i-=1
print(d,c,u)