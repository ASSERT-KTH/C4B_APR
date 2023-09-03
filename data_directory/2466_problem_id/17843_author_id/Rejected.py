def main():
	path = input()
	if isValid(path):
		print("OK")
	else:
		print("BUG")

def isValid(s):
	positions = set()
	current = (0, 0)
	positions.add(current)
	for c in s:
		if c == 'L':
			current = left(current)
		elif c == 'R':
			current = right(current)
		elif c == 'U':
			current = up(current)
		elif c == 'D':
			current = down(current)
		else:
			assert(False)
		positions.add(current)
		# check if all 4 directions for a cycle
		count = 0
		if left(current) in positions:
			count += 1
		if right(current) in positions:
			count += 1
		if up(current) in positions: 
			count += 1
		if down(current) in positions:
			count += 1
		if count > 1:
			return False
	return True

def left(point):
	return (point[0] - 1, point[1])	

def right(point):
	return (point[0] + 1, point[1])

def up(point):
	return (point[0], point[1] + 1)

def down(point):
	return (point[0], point[1] - 1)

main()
#print(isValid("RRUULLDD"))