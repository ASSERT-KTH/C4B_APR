x,y = [int(x) for x in raw_input().split(" ")]

n = 0

while x <= y:
	n += 1
	x *= 3
	y *= 2

print(n)