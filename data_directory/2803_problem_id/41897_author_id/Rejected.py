n,k=list(map(int,input().strip().split(' ')))
L=n//k
if k*(k+1)//2>n:
    print(-1)
else:
    temp=(k*(k+1))//2
    L=n//temp
    while(n%L!=0):
        L-=1
    T=(n-((temp)*L))//L
    ans=[]
    for i in range(1,k+1):
        if i!=k:
            ans+=[i*L]
        else:
            ans+=[(i+T)*L]
    print(*ans)