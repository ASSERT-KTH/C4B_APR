n,a,b,c=map(int,input().split())
n=n%4
if(n==0):
	print(0)
elif(n==1):
	print(min(3*a,a+b,c))
elif(n==2):
	print(min(2*a,b,2*c))
elif(n==3):
	print(min(a,b+c,9*c))