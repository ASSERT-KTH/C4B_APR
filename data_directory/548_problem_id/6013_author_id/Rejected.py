n,m=map(int,input().split(' '))
i=1;k=0
while(i<=n):
  j=1
  while(j<=m):
     if((i+j)%5==0):
        k=k+1
     j=j+1
  i=i+1   
print(k)