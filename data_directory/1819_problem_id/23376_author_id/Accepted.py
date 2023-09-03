# y, k, n = a[0], a[1], a[2]
s = input()
a = []
a = s.split()

for i in range(len(a)):
	a[i] = int(a[i])
	
b = []
i = 1
while a[1]*i <= a[2]:
	if (a[1]*i > a[0]):
		b.append(a[1]*i-a[0])
	i += 1

if len(b) == 0:
	print(-1)
else:
	for i in range(len(b)):
		print(b[i], end = ' ')