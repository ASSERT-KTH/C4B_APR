l,r,k=map(int,input().split())
s=""
for i in range(500):
    if k**i<=r and k**i>=l:
        s+=str(k**i)+" "
if len(s)>0:
    print(s)
else:
    (print(-1))