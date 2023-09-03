n = int(input())
s = input()
a = []
a = s.split()
for i in range(len(a)):
	a[i] = int(a[i])

i = 0
while n > 0:
	n -= a[i]
	i += 1
	if i>6:	i = 0
	
if i==0: print(7)
else: print(i)