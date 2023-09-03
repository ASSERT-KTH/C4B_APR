'''input
14 28
'''
n, m = map(int, input().split())
t = 0
for a in range(100000):
	if a + n**2 - 2*n*a**2 + a**4 == m:
		t += 1
print(t)