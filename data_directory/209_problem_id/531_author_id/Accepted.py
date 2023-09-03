'''input
1 1000000
'''
a, b = map(int, input().split())
s = 0
n = str(list(range(a, b+1)))
d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for x in range(10):
	s += d[x] * n.count(str(x))
print(s)