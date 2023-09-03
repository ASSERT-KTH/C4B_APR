n, k = [int(x) for x in input().split(' ')]

symbols = 'abcdefghijklmnopqrstuvwxyz'
newPsw = ''
q = 0
for i in range(n):
	if q == k:
		q = 0
	newPsw += symbols[q]
	q += 1
print(newPsw)