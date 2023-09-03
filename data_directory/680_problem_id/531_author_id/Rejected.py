'''input
3
'''
n = int(input())
if n <= 2:
	print(-1)
else:
	if n % 3 == 0:
		print(4*n//3, 5*n//3)
	elif n % 4 == 0:
		print(3*n//4, 5*n//4)
	elif n % 5 == 0:
		print(3*n//5, 4*n//5)
	else:
		t = 1
		while n % 2 == 0:
			t *= 2
			n //= 2
		x = n // 2 - 1
		while 2*x + 1 != n**2:
			x += 1
		print(t*x, t*(x+1))