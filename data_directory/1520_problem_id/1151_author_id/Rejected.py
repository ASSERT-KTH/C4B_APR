def f(n,a,b,c):
    global ans,k
    k+=1
    if n-a>0:
        n-=a
        f(n,a,b,c)
    elif n-a==0:
        ans.append(k)
    if n-b>0:
        n-=b
        f(n,a,b,c)
    elif n-b==0:
        ans.append(k)
    if n-c>0:
        n-=c
        f(n,a,b,c)
    elif n-c==0:
        ans.append(k)

n,a,b,c=list(map(int,input().split()))
ans=[]
k=0
if n%min(a,b,c)==0:
    print(n//min(a,b,c))
else:
    f(n,a,b,c)
    print(max(ans))