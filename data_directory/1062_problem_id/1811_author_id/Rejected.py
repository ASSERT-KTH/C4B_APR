n = str(input().strip())

if len(n) == 4 or len(n) == 7:
	for i in n:
		if i == '7' or i == '4':
			fl = True
		else:
			fl = False
			break
else:
	fl = False

if fl == True:
	print('YES')
else:
	print('NO')