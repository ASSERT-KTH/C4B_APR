a=input().split(' ')
b=input().split(' ')

if (int(a[2])-int(a[0]))%int(b[0])!=0 or (int(a[3])-int(a[1]))%int(b[1])!=0:
	print ('NO')

elif (int(a[2])-int(a[0]))//int(b[0])%2== (int(a[3])-int(a[1]))//int(b[1])%2:
	print ('YES')

else:
	print ('NO')