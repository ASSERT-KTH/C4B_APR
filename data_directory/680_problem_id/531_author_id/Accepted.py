'''input
3
'''
n = int(input())
if n <= 2:
	print(-1)
else:
	if n % 2 == 0:
		print(n**2//4-1, n**2//4+1)
	else:
		print((n**2-1)//2, (n**2+1)//2)