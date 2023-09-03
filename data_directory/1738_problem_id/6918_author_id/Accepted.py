import sys
x,y,z = map(int, input().split())
for a in range(1,10001):
	if x%a==0:
		b=x//a
		if y/b==z/a:
			print(4*(a+b+y//b))
			sys.exit()