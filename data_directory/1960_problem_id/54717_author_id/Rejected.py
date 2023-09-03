row1 = input().split()
print(row1)
row2 = input().split()
print(row2)
row3 = input().split()
print(row3)
row4 = input().split()
print(row4)
row5 = input().split()
print(row5)

x = 0
y = 0

for i in range(5):
	try:
		if i == 0:
			y = row1.index('1') + 1
			print("found in row " + str(i + 1))
			x = 1
			break
		elif i == 1:
			y = row2.index('1') + 1
			print("found in row " + str(i + 1))
			x = 2
			break
		elif i == 2:
			y = row3.index('1') + 1
			print("found in row " + str(i + 1))
			x = 3
			break
		elif i == 3:
			y = row4.index('1') + 1
			print("found in row " + str(i + 1))
			x = 4
			break
		elif i == 4:
			y = row5.index('1') + 1
			print("found in row " + str(i + 1))
			x = 5
			break	
	except ValueError as e:
		print("Not found")
		pass

print(x)
print(y)

xdiff = abs(3 - x)
ydiff = abs(3 - y)

print(xdiff)
print(ydiff)

moves = xdiff + ydiff
print(moves)