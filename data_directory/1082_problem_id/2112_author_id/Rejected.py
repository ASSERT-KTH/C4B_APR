k, l = int(input()), int(input())

x = 0
while k < l:
	k *= k
	x += 1

if k == l:
	print("YES")
	print(x)
else:
	print("NO")