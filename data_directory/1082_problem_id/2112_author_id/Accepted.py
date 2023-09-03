k, l = int(input()), int(input())

x, t = 0, k
while t < l:
	t *= k
	x += 1

if t == l:
	print("YES")
	print(x)
else:
	print("NO")