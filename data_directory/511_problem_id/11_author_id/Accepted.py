a,b,c=map(int,input().split())
if c==0 and a==b:exit(print("YES"))
elif c==0 and a!=b:exit(print("NO"))
l,r=0,2*10**9
while l<=r:
  mid=(l+r)//2
  s=a+mid*c
  if s==b:exit(print("YES"))
  elif s>b:
    if c>0:r=mid-1
    else:l=mid+1
  else:
    if c>0:l=mid+1
    else: r=mid-1 
print("NO")