p,q=input().split()
p=int(p)
q=int(q)
high=max(p,q)
low=min(p,q)
if(p==q):
    print("%d %d"%(high-1,low))
else:
    if(low>2):
        print("%d %d"%(high-low,low))
    else:
        print("%d %d"%(high-1,low))