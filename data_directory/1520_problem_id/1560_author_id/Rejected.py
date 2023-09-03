a=input()
b=a.split()
c=[]
i=1
while i<4:
	c.append(int(b[i]))
	i+=1

max=0
n=int(b[0])
for x in range(0,n//c[0]+1):
	for y in range(0,(n-x*c[0])//c[1]+1):
		if (n-(x*c[0]+y*c[1]))%c[2]==0:
			if max<x+y+(n-(x*c[0]+y*c[1]))//c[2]:
				max=x+y+(n-(x*c[0]+y*c[1]))//c[2]

print(max)