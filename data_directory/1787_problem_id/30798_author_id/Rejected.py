n=int(input())
x=[]
if (n==1):
	print(-1)
else:
	i=1
	while(i<n):
		print(i+1,end=' '),
		print(i,end=' '),
		i=i+2
	if (i==n):
		print(i,end=' ')
	print('')