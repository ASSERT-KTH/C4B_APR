'''input
4
'''
n = int(input())
if n == 0:
	print(-1)
else:
	for x in range(n//4+1):
		for y in range(n//7+1):
			if 4*x + 7*y == n:
				print("4" * x + "7" * y)
				quit()
	print(-1)