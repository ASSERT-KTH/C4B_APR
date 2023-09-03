# y, k, n = a[0], a[1], a[2]
s = input()
a = []
a = s.split()

for i in range(len(a)):
	a[i] = int(a[i])
	
b = []
for i in range(1, a[2]-a[0]+1):
	if ((a[0]+i) % a[1]) == 0:
		b.append(i)

if len(b) == 0:
	print(-1)
else:
	for i in range(len(b)):
		print(b[i], end = ' ')