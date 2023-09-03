'''input
4 4
'''
a1, a2 = map(int, input().split())
if a1 == a2 == 1:
	print(0)
	quit()
if a1 > a2:
	a1, a2 = a2, a1
t = 0
while a1 > 0:
	a1 += 1
	a2 -= 2
	t += 1
	if a1 > a2:
		a1, a2 = a2, a1
print(t)