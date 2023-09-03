k=int(input())
b=input().split()
a=[]
for i in b:
	a.append(int(i))
sum=0
for i in a:
	sum+=i
if k>sum:
	print('-1')
else:
	count=0
	while k>0:
		k-=max(a)
		a.remove(max(a))
		count+=1
	print(count)