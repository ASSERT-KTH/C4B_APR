l=list(map(int,input().split(" ")))
t=l[0]
s=l[1]
x=l[2]
if x==t:
	print("YES")
elif ((x-t)%s==0 and (x-t)>0) or ((x-t-1)%s==0 and (x-t-1)>0):
	print("YES")
else:
	print("NO")