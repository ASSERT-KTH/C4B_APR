p,q=input().split()
p=int(p)
q=int(q)
high=max(p,q)
low=min(p,q)
print("%d %d"%(p+q-1-low,low))