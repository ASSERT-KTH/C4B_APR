def fact(n):
  b=[0]*(n+1)
  b[1]=1
  for i in range(2,n+1):
    b[i]=i*b[i-1]
  return b[n]
def gcd(a,b):
  while(b):
    a,b=b,a%b
  return a
n,k =map(int,input().split(' '))
print(gcd(fact(n),fact(k)))