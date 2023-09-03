'''input
433
109 58 77 10 39 125 15 
'''
n = int(input())
a = list(map(int, input().split()))
n %= sum(a)
if n == 0:
	n += sum(a) 
s = 0
for x in range(7):
	s += a[x]
	if s >= n:
		print(x+1)
		break