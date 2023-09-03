n=int(input())
m=1
M=10**8
mid=(m+M)//2
s=((mid)*(mid+1)//2)
s1=s+mid+1
while not (s<=n and s1>n):
    mid=(m+M)//2
    s=((mid)*(mid+1)//2)
    s1=s+mid+1
    if s<n and s1<n:
        m=mid
    elif s>n:
        M=mid
    elif s<=n and s+mid+1>n:
        break
    #print(mid)
if s==n:
    print(mid)
else:
    print(n-s)