'''input
2
3
4
5
24
'''
k, l, m, n, d = [int(input()) for _ in range(5)]
unharmed = 0
if min([k,l,m,m]) == 1:
	print(d)
else:
	for x in range(1,d+1):
		if all(x % i != 0 for i in [k,l,m,n]):
			unharmed += 1
	print(d-unharmed)