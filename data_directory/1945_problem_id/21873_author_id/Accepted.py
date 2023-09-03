a,b,n=map(int,input().split())
a=a*10
for i in range(0,10):
	if((a+i)%b==0):
		break
if(i==9 and (a+9)%b!=0):
	print(-1)
else:
	a=a+i
	print(a,end='')	
	while(n>1):
		print(0,end='')
		n=n-1