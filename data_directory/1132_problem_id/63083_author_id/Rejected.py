n = int(input())
flag = 0
if n % 4 == 0 or n % 7 == 0:
	print('YES')
else:
	string = str(n)
	for i in string:
		if i == '4' or i == '7':
			continue
		else:
			print('NO')
			flag = 1
			break
	if flag == 0:
		print('YES')