s = input()
a = []
for i in range(len(s)):
	a.append(s[i])

if ('H' in a) or ('Q' in a) or ('9' in a):
	print('YES')
else:
	print('NO')