import sys

def sol(n):
	if n%2==0 and n>=4:
		print('YES')
		return 'YES'
	else:
		print('NO')
		return 'NO'

sol(int(sys.argv[0]))