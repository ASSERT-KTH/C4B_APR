a = input()
x = list()
flag=0
for i in range(0,len(a)):
	if a[i]=='4' or a[i]=='7':
		flag+=1
if flag==4 or flag==7:
	print("YES")
else:
	print("NO")