s = input()

sum0 = 0
sum1 = 0
for i in range(len(s)):
	if s[i] == '0': 
		sum0 += 1
	if s[i] == '1':
		sum1 += 1

if (sum0 == 7) or (sum1 == 7):
	print('YES')
else:
	print('NO')