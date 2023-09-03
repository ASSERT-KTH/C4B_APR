n,m,k=[int(f)for f in input().split()]
l,r=0,m
t=True
for x in range(60):
    i=(l+r)//2
    c=k-1
    b=n-k
    s=i-1+n+[(i-2-b)*b if i-2-b>0 else 0][0]+[(i-2-c)*c if i-2-c>0 else 0][0]+(min(i-2,b))*(1+min(b,i-2))/2+(min(i-2,c))*(1+min(c,i-2))/2
    if n==1:
        print(m)
        t=False
        break
    if s<=m:
        l=i
    elif s>=m:
        r=i
    #print(s,m,l,r,i)
if t:print(l)