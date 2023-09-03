p=int(input())
x=0
while p:
	p=p-1
	x=x+1
	if p<=1:
		break
	p=p-2
	x=x+1
print(x)