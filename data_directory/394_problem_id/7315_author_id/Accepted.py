n,k=list(map(int,input().split()))
ans=n*(n-1)//2
if k>=n//2:
    print(ans)
else:
    m=n-2*k
    ans=ans-m*(m-1)//2
    print(ans)