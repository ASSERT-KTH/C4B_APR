k = int(input())
s = input()
a = s.split()
for i in range(len(a)):
	a[i] = int(a[i])
	
a.sort()
a.reverse()
sum = 0
while k>0 and len(a)>0:
	k -= a[0]
	a.remove(a[0])
	sum += 1
if k > 0:
	print(-1)
else:
	print(sum)