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
	surplus = ((a - x) // 2) + ((b - y) // 2) + ((c - z) // 2)
	# print("surplus:", surplus)
	need = (x-a) + (y-b) + (z-c)
	# print("need:", need)
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