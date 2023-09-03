'''input
17851817
'''
n = int(input())
for x in range(1500):
	for y in range(1500):
		if (n - 1234567*x - 123456*y) > 0 and (n - 1234567*x - 123456*y) % 1234 == 0:
			print("YES")
			quit()
print("NO")