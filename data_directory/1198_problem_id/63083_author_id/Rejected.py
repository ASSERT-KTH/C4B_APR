line = input()
if 'H' in line or 'Q' in line or '9' in line:
	print('YES')
elif '+' in line:
	occ = line.count('+')
	if occ == 15 or occ == 30 or occ == 39:
		print ('YES')
	else:
		print('No')
else:
	print('NO')