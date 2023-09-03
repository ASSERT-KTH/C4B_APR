from math import factorial as f
k=int(input())
n=2*k-1
ans=2*(f(n))//(f(k)*f(n-k))
print((ans-k)%1000000007)