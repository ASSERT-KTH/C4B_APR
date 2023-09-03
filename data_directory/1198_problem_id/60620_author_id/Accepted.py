s = list(input())

i = ['H', 'Q', '9']
if any([x for x in i if x in s]):
	print('YES')
else:
	print('NO')