s = input().strip()

pi = ('H', 'Q', '9', '+')

for i in s:
	if i in pi:
		f = True
		print('YES')
		quit()
	else:
		f = False

if f == False:
	print('NO')