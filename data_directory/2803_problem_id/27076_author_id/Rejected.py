n,k=map(int,input().split())
nod=-1
d=1
while d*d<=n:
    s=d*(k-1)*k//2
    if n-s>(k-1)*d:
        if (n-s)%d==0: nod=d
    d+=1
ans=""
if nod>-1:
    for i in range(1,k):
        ans+=str(nod*i)+' '
    print(ans+str(n-nod*(k-1)*k//2))
else:
    print(-1)