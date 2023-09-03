s = input()
a = []
for i in range(len(s)):
	a.append(s[i])

while len(a) > 0:
	if (a[0] == 'H') or (a[0] == 'Q') or (a[0] == '9') or (a[0] == '+'):
		print('YES')
		break
	else:
		a.remove(a[0])
	if len(a) == 0:
		print('NO')