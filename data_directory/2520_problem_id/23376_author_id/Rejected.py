a = []
s = input()
a = s.split()
for i in range(len(a)):
	a[i] = int(a[i])

ma = max(a[0], a[1])
mi = 6-ma+1

def uc(a, b):
	while a != b:
		if a>b:
			mid = b
			b = a-b
			a = mid
		else:
			mid = a
			a = b-a
			b = mid
	return a

if mi == 6:
	print(1)
else:
	print(int(mi/uc(mi, 6)), end = '')
	print('/', end = '')
	print(int(6/uc(mi, 6)), end = '')