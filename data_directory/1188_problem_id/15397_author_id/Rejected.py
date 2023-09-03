from math import factorial as fact
def c(x,y):
	return fact(x)//(fact(y)*fact(x-y));

n,m,t=[int(i) for i in input().split()]
if (n<4) or (m<1):
	print(0)
	exit(0)
res=0
for i in range(4,n+1):
	if t-i<=m:
		res+=c(n,i)*c(m,t-i)
	
print(res,sep='',end='')