'''input
999999999 1000000000 1000000000 1000000000
'''
n, a, b, c = map(int, input().split())
n = n % 4
if n == 0:
	print(0)
elif n == 1:
	print(min([c, a+b, 3*a]))
elif n == 2:
	print(min([b, 2*a, 2*c]))
elif n == 3:
	print(min([a, b+c]))