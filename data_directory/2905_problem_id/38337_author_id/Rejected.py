m,b=map(int,input().split())
x=[]
y=[]
t=b
i=0
maxnum=0
while t>0:
	num=0
	x.append(i*m)
	y.append(b-i)
	t=y[i]
	for j in range(x[i]+1):
		for k in range(y[i]+1):
			num+=j+k
	maxnum=max(maxnum,num)
	i+=1
	pass
print(maxnum)