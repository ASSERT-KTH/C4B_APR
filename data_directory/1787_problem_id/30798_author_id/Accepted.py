n=int(input())
x=[]
if (n%2!=0):
	print(-1)
else:
	for i in range(int(n/2)):
		print(i*2+2,end=' ')
		print(i*2+1,end=' ')
	print('')