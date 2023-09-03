s=input()
n=len(s)
com='hello'
j=0
if n<5:
	print('NO')
else:
	for i in s:
		if com[j]==i:
			j+=1
		if j>=4:
			break;
	if j>4:
		print('YES')
	else:
		print('NO')