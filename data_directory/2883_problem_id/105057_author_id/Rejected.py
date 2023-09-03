a=input().split(' ')
b=input().split(' ')

if int(a[2])%int(b[0])==0 and int(a[3])%int(b[1])==0:
	print ('YES')

else:
	print ('NO')