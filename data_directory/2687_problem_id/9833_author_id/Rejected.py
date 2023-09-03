n,m=map(int,input().split())
if n<=m:
    print(n)
else:
    lo=1
    hi=int(2e9)
    while lo<hi:
        mid=(lo+hi)//2
        val=((mid+1)*mid)//2
        val1=((mid-1)*mid)//2
        if n-val>m:
            lo=mid
        elif n-val<m and n-val1<m:
            hi=mid
        else:
            break
    print(m+mid)