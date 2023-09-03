'''input
10
'''
n = int(input())
for x in range(1, n//4+1):
	for y in range(1, n//7+1):
		if 4*x + 7*y == n:
			print("4" * x + "7" * y)
			quit()
print(-1)