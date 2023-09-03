n,a,b=map(int,input().split())
if(((a+b)%n)%n==0):print(n)
else:
  print(((a+b)%n)%n)