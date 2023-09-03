'''input
1358023
'''
n = int(input())
for x in range(n//1234567+1):
	for y in range(n//123456+1):
		if (n - 1234567*x - 123456*y) >= 0 and (n - 1234567*x - 123456*y) % 1234 == 0:
			print("YES")
			quit()
print("NO")