'''input
1 11
'''
n, m = map(int, input().split())
t = 0
for a in range(10000):
	if a + n**2 - 2*n*a**2 + a**4 == m and n - a**2 >= 0:
		t += 1
print(t)