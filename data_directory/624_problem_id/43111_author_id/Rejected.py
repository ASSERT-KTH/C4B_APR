t, s, x = list(map(int, input().split()))

if x < t:
	print("NO")
else:
	x -= t
	if x % s == 0 or x % s == 1:
		print("NO")
	else:
		print("YES")