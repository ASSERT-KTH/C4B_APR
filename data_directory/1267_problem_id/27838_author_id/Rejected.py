def solve(n,s):
	st = set(str(int(s)))
	arr = [int(i) for i in st]
	if len(arr) > 2:
		print('NO')
	elif len(arr) == 1 and arr[0] != 4 and arr[0] != 7:
		print('NO')
	elif len(arr) == 2 and arr[0] * arr[1] != 28:
		print('NO')
	else:
		x = sum([int(s[i]) for i in range(n//2)])
		y = sum([int(s[i]) for i in range(n//2,n)])
		if x == y:
			print('YES')
		else:
			print('NO')

n = int(input())
num = input()

solve(n,num)