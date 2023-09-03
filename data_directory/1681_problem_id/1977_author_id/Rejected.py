c=0
n,m=map(int,input().split())
p=max(m,n)
for i in range(p+1):
  if (i*i+(n-(i*i)))==n and (i+(n-i)*(n-i))==m:
    c=c+1
print(c)