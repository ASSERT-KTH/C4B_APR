a,b,n=map(int,input().split())
temp=0
count=0
def gcd(x,y):
	if(y==0):
		return x
	else:
		return gcd(y,(x%y))
while(1<2):
	temp=gcd(a,b)
	if(temp>n):
		break
	else:
		n-=temp
		count+=1
print((count+1)%2)