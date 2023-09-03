def tri(a, b, c, d):
	if ((a + b > c) and (a + c > b) and (b + c > a) or ((d + b > c) and (d + c > b) and (b + c > d)) or (( a+ d > c) and (a + c > d) and ( d + c > a)) or ((a + b > d) and (a + d > b) and (b + d > a))):

		print("TRIANGLE")
	else:
		if ((a + b == c) or (a + c == b) or (b + c == a) or (d + b == c) or (d + c == b) or (b + c == d) or (a + d == c) or (a + c == d) or (d + c == a) or (a + b == d) or (b + d == a) or (a + d == b)):
			print("SEGMENT")
		else:
			print("IMPOSSIBLE")
a, b, c, d= map(int, input().split(' '))
tri(a,b,c,d)