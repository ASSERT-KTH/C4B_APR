s = input()
a = []
a = s.split()

for i in range (len(a)):
	a[i] = int(a[i])

def fac(x):
	sum = 1
	for i in range(1,x+1): sum *= i
	return sum

if a[0] < a[1]:
	print(fac(a[0]))
else:
	print(fac(a[1]))