a=list(input().split())

a[0]=int(a[0])
a[1]=int(a[1])
stos=int(a[2])


def gcd(x,y):
	while y:
		x,y=y,x%y
	return x

res=True

while True:
	t=gcd(a[res],stos)
	if stos-t<0:
		print(int(res))
		break
	else:
		stos-=t
	res = not res