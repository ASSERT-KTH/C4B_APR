c = 0
h = "hello"

for i in input():
	if i == h[c]:
		c += 1
		if c == 5:
			print("YES")
			break
else:
	print("NO")