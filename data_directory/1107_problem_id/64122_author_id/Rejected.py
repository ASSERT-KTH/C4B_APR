def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)
a,b,n=[int(i) for i in input().split()]
i=1
if n<a:
    i=1
while n>=max(a,b):
    if i%2==1:
        n=n-gcd(n,a)
    elif i%2==0:
        n=n-gcd(n,b)
    i=i+1
if i%2==1:
    print(1)
else:
    print(0)