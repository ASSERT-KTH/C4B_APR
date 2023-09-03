n,a,b,c=map(int,input().split())
l=[-1]*8001
l[0]=0
for i in range(1,n+1):
    if max(l[i-a],l[i-b],l[i-c])>-1:
        l[i]=max(l[i-a],l[i-b],l[i-c])+1

print(l[n])