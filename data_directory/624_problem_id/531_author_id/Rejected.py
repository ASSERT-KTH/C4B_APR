'''input
3 10 4
'''
t, s, x = map(int, input().split())
if ((x-t) % s == 0 or (x-t-1) % s == 0) and x-t != 1:
	print("YES")
else:
	print("NO")