import sys

#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

def prime(n):
	for i in range(2, n):
		if i * i > n:
			break
		if divmod(n, i)[1] == 0:
			return False
	if n > 1:
		return True
	else:
		return False

def solve(n):
	ans = 0
	for i in range(2, n + 1):
		c = 0
		for j in range(2, i + 1):
			if prime(j) and divmod(i, j)[1] == 0:
				c += 1
		if c == 2:
			ans += 1
	return ans

n = int(input())
print(solve(n))