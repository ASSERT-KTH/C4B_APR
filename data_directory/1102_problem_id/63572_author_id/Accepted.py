a=input()
a=a.lower()
b=["a","e","i","o","u","y"]
c=[]
for i in range(len(a)):
	if(a[i] not in b):
		c.append(".")
		c.append(a[i])
for i in c:
	print(i,end="")
print("\n")