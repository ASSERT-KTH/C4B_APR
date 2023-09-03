# n = int(input())
# flag = 0
# if n % 4 == 0 or n % 7 == 0:
# 	print('YES')
# else:
# 	string = str(n)
# 	for i in string:
# 		if i == '4' or i == '7':
# 			continue
# 		else:
# 			print('NO')
# 			flag = 1
# 			break
# 	if flag == 0:
# 		print('YES')
n = int(input())
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
flag = 0
for i in lucky_numbers:
	if n % i == 0:
		print('YES')
		flag = 1
		break
if flag == 0:
	print('NO')