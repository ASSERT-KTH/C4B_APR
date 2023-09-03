a,b=map(int,input().split())
if(a==0 and b==0):
	print('NO')
	exit(0)
if(abs(a-b)<=1):
	print('YES')
else:
	print('NO')