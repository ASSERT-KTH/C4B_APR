def main():
	p, k = map(int, input().split())
	s = 1
	m = 10**9+7
	if k == 0:
		for _ in range(p-1):
			s *= p %m
	elif k == 1:
		for _ in range(p):
			s *= p %m
	else:
		o = 1
		n = k
		while n != 1:
			n = k*n %p
			o += 1
		c = (p-1)//o
		for _ in range(c):
			s = s*(1+c*o) %m
	print(s%m)
main()