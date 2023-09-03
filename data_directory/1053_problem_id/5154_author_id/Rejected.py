n=int(input())
ot='-1'
for i in range(n//7+1):
	o=n-(7*i)
	if(o%4==0):
		ot=''
		for j in range(o//4):ot=ot+'4'
		for j in range(i):ot=ot+'7'
print(ot)