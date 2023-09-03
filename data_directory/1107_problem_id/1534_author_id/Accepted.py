def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

a,b,n=map(int,input().split())
count=0
while(1<2):
	if n==0:
		print(1-int(count%2))
		break
	else:
		if count%2==0:
			n-=gcd(n,a)
			count+=1
		else:
			n-=gcd(n,b)
			count+=1