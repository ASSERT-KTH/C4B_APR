k=int(input())
b=int(input())
n=int(input())
t=int(input())
stock=1
while(k*stock+b<=t and n>0):
    stock=k*stock+b
    n-=1
print(n)