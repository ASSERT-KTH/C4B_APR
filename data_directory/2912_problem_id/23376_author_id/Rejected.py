s = input()
a = []
a = s.split()

for i in range (len(a)):
	a[i] = int(a[i])

def fac(x):
	sum = 1
	for i in range(1,x+1): sum *= i
	return sum

def gcd(x, y):
	while x != y:
		if x > y:
			x -= y
		else:
			y -= x
	return x

m = fac(a[0])	
n = fac(a[1])
print(gcd(m, n))