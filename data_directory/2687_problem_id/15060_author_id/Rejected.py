n,m=input().split()
n=int(n)
m=int(m)
if(m>=n):
    m=n
    print(n)
else:
    a=2*(n-m)
    u=1
    l=n-1-m
    while(u!=l):
        mid=(u+l)//2
        if(mid*(mid+1)>=a):
            if((mid-1)*mid<a):
                break
            else:
                l=mid-1
        else:
            if((mid+1)*(mid+2)>=a):
                mid+=1
                break
            else:
                u=mid+1
    print(mid+m)