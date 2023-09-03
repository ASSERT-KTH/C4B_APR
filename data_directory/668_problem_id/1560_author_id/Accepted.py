a=int(input())
b=a
str=''
while b>0:
	if b>1:
		if (a-b)%2==0:
			str+='I hate that '
			b-=1
		else:
			str+='I love that '
			b-=1
	else:
		if (a-b)%2==0:
			str+='I hate it '
			b-=1
		else:
			str+='I love it '
			b-=1 
print(str)