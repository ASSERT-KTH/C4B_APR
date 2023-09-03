k = int(input())
s = input()
a = s.split()
for i in range(len(a)):
	a[i] = int(a[i])
	
a.sort()
a.reverse()
sum = 0
while k>0:
	k -= a[0]
	a.remove(a[0])
	sum += 1

print(sum)