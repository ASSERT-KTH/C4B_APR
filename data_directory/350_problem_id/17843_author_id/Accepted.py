def main():
	(n, k) = (int(x) for x in input().split())
	print(solver(n, k))

def solver(n, k):
	if k >= n // 2:
		return n * (n - 1) // 2
	else:
		return k * (2 * n - 2 * k - 1)

#print(solver(100, 2))
main()