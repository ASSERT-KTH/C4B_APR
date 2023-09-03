s = str(input())
if s.isupper():
	print(s)
else:
	print(s[0].upper(), end = '')
	for i in range(1, len(s)):
			print(s[i].lower(), end ='')