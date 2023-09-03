n=int(input())
l=[1,2,3,4,5]
drink=0
for i in range(1,n+1):
	drink=l[0]
	l.append(drink)
	l.append(drink)
	del(l[0])
if drink==1:
	print("Sheldon")
elif drink==2:
	print("Leonard")
elif drink==3:
	print("Penny")
elif drink==4:
	print("Rajesh")
elif drink==5:
	print("Howard")