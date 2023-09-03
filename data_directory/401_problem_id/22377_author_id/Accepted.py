a=int(input())
x=0
if(a<0):
	exit(0)
if(a<13):
	x=2**a
	print(x)
else:
	x=8092*(2**(a-13))
	print(x)