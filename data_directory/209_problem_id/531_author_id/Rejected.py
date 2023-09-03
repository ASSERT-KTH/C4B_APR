'''input
10 15
'''
a, b = map(int, input().split())
s = 0
d = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}
for x in range(a, b+1):
	for l in str(x):
		s += d[l]
print(s)