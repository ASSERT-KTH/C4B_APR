a, b = map(int, input().split())
c, d = map(int, input().split())
if b == d:
	print(b)
else:
	s = set()
	for i in range(0, 101):
		s.add(b + a * i)
	for i in range(0, 101):
		temp = d + c * i
		if temp in s:
			print(temp)
			exit(0)
	print(-1)