'''input
4 6 6
'''
def gcd(x, y):
	while y != 0:
		x, y = y, x % y
	return x
a, b, c = map(int, input().split())
l = a * b // gcd(a, b)
l = l * c // gcd(l, c)
x = (l // a + l // b + l // c)
if len(set([a, b, c])) < 3:
	print(4*x)
else:
	print(8*x)