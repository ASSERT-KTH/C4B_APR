n=input()
n=int(n)
i=0
list1=['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
while i<n:
	var1=list1[i]
	i=i+1
	list1.append(var1)
	list1.append(var1)
print(list1[n-1])