a, b, c = map(int, input().split(' '))
i = a
l = list()

if a == b and c == 0:
	print('YES')
elif a != b and c == 0:
	print('NO')
else:
	if b >= 0:		
		while i <= b:
			l.append(i)
			i += c
	else:
		while i >= b:
			l.append(i)
			i += c
	if b in l:
		print('YES')
	else:
		print('NO')