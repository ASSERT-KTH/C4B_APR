"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""

def main():
	n, R, r = map(int, input().split())

	if n == 1:
		if r <= R: print('YES')
		else: print('NO')
	else:
		import math
		# calculate side of inscribed n-gon
		a = (R - r) * math.sin(math.pi / n)
		if r < a+1e-6: print('YES')
		else: print('NO')


if __name__ == '__main__':
    main()