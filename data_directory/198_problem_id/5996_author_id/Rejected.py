a=[0]
for _ in range(int(input())):
	x=1
	while a[-1]==x:
		x+=a.pop()
	a+=[x]
print(*a[1:])