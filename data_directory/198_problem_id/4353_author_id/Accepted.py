n=int(input())
for i in range(20,-1,-1):
 if 2**i<=n:
  print(i+1,end=" ")
  n-=2**i