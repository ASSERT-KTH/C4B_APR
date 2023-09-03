import sys
x,y,z = map(int, input().split())
for a in range(5000):
	for b in range(5000):
		if a*b==x and y/b==z/a:
			print(4*(a+b+y//b))
			a=5000
			sys.exit()