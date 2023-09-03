'''input
3
8
'''
k, l = int(input()), int(input())
for x in range(1, 100):
	if k**x == l:
		print("YES")
		print(x-1)
		break
else:
	print("NO")