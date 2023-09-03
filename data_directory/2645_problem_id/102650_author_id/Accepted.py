n=int(input())
x=int(input())

shell=[0,0,0]
shell[x]=1

n=n%6

while n>0:
	if n%2==1:
		temp=shell[0]
		shell[0]=shell[1]
		shell[1]=temp
	else :
		temp=shell[1]
		shell[1]=shell[2]
		shell[2]=temp
	n-=1

i=0
while i<3:
	if shell[i]==1:
		print(i)
		break
	i+=1