s = input()
a = 0
for i in range(len(s)):
	if (s[i] == '4') or (s[i] == '7'):
		a += 1

if len(s) == a:
	print('YES')
else:
	print('NO')