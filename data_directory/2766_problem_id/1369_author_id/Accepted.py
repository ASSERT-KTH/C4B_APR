import copy
s=list(input())
a=copy.copy(s)
a.reverse()
k=len(s)
total=0
for i in range(0,k):
	if s[i]!=a[i]:
		total=total+1
	if total>2:
		print("NO")
		break
if total==2:
	print("YES")
elif total==0 and k%2==1:
	print("YES")
elif total<2:
	print("NO")