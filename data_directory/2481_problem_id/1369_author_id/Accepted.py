n=int(input())
x=0
total=0
while(1>0):
	if total>=n:
		break
	s=total
	total=total+5*pow(2,x)
	x=x+1
t=(n-s)/pow(2,x-1)
if t<=1:
	print("Sheldon")
elif t>1 and t<=2:
	print("Leonard")
elif t>2 and t<=3:
	print("Penny")
elif t>3 and t<=4:
	print("Rajesh")
elif t>4 and t<=5:
	print("Howard")