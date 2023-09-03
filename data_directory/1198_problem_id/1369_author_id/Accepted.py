a=input()
f=0
for i in a:
	if i=="H" or i=="Q" or i=="9":
		f=1
		print("YES")
		break
if f==0:
	print("NO")