a=list(input().split())

a[0]=int(a[0])
a[1]=int(a[1])
stos=int(a[2])


def gcd(x,y):
	while y:
		x,y=y,x%y
	return x

res=False

while True:
	t=gcd(a[res],stos)
	#print(a[res], stos, t)
	if stos-t<0:
		print(int(not res))
		break
	else:
		stos-=t
	res = not res