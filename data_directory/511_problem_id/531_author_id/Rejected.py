'''input
1 7 3
'''
a, b, c = map(int, input().split())
if a == b:
	print("YES")
elif c == 0:
	print("NO")
elif (b-a) % c == 0 and b > a and c > 0:
	print("YES")
elif (b-a) % c == 0 and c < 0:
	print("YES")
else:
	print("NO")