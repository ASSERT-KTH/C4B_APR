f=lambda a, b: a if b==0 else f(b, a%b)
a,b,n = map(int,input().split())
c=1
while n>0:
	c =  0 if c else 1
	n -= f(b,n) if c else f(a,n)
print(c)