n=eval(input())
while(n>0):
	k=n%10
	if(k!=4 and k!=7):
		print("NO")
		break
	n=n//10
else:
	print("YES")