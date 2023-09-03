#Justin Hershberger
#Py3.5

import fileinput

def test():
	pass
if __name__ == '__main__':
	num_args = 2
	for arg in range(num_args):
		if arg == 0:
			a,b,c = map(int, input().split())
		else:
			x,y,z = map(int, input().split())
    # ax = x - a
	# by = y - b
	# cz = z - c
	abc = [a, b, c]
	xyz = [x, y, z]
	need = 0
	surplus = 0

	for i in range(0, 3):
		if xyz[i] - abc[i] > 0:
			need += xyz[i] - abc[i]
		else:
			surplus += (abc[i] - xyz[i]) // 2
	# surplus = ((a - x) // 2) + ((b - y) // 2) + ((c - z) // 2)
	if surplus >= need and surplus >= 0:
		print("Yes")
	else:
		print("No")


	#
	# sum3 = (a - x) + (b - y) + (c - z)
	# if x <= a and y <= b and z <= c:
	# 	print("Yes")
	# elif (x > a and y > b) or (x > a and z > c) or (y > b and z > c):
	# 	sum1 = (x - a) + (y - b) + (z - c)
	# 	if sum1 < 0:
	# 		print("No")
	# elif (x - a > 0) and (((b-y) // 2 + (c-z) // 2) >= (x-a)):
	# 	print("Yes")
	# elif (y - b > 0) and (((a-x) // 2 + (c-z) // 2) >= (y-b)):
	# 	print("Yes")
	# elif (z - c > 0) and (((b-y) // 2 + (a-x) // 2) >= (z - c)):
	# 	print("Yes")
	# else:
	# 	print("No")

	# if x <= a and y <= b and z <= c:
	# 	print("Yes")
	# elif (sum3 < 0):
	# 	print("No")
	# else:
	# 	print("Yes")