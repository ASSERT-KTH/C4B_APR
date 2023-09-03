l=list(map(int,input().split(" ")))
a=l[0]
b=l[1]
c=l[2]
d=b-a
if d==0:
	print("YES")
elif c!=0:
	if d%c==0 and d*c>0:
		print("YES")
	else:
		print("NO")
else:
	print("NO")