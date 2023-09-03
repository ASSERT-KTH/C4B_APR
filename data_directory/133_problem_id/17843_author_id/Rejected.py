def main():
	(a, b, c) = (int(n) for n in input().split())
	(x, y, z) = (int(n) for n in input().split())
	if solver(a, b, c, x, y, z):
		print("Yes")
	else:
		print("No")

# def solver(a, b, c, x, y, z):
# 	if a >= x:
# 		if b >= y:
# 			if c >= z:
# 				return True
# 			else:
# 				return min(a - x, b - y) > z - c
# 		else:
# 			if c >= z:
# 				return min(a - x, c - z) > y - b
# 			else:
# 				return "No"
# 	else:
# 		if b >= y and c >= z:
# 			return min(b - y, c - z) > a - x

def solver(a, b, c, x, y, z):
	if a >= x and b >= y and c >= z:
		return True
	elif a >= x and b >= y and c < z:
		return (a - x) // 2 + (b - y) // 2 >= z - c
	elif a >= x and b < y and c >= z:
		return (a - x) // 2 + (c - z) // 2 >= y - b
	elif a < x and b >= y and c >= z:
		return (b - y) // 2 + (c - z) // 2 >= x - a
	elif a < x and b < y and c >= z:
		return (z - c) // 2 >= x - a + y - b
	elif a < x and b >= y and c < z:
		return (b - y) // 2 >= x - a + z - c
	elif a >= x and b < y and c < z:
		return (a - x) // 2 >= y - b + z - c
	else:
		return False


		

#print(solver(4, 4, 0, 2, 1, 2))
#print(solver(5, 6, 1, 2, 7, 2))			
main()