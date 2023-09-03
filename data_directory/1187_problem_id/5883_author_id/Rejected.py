s = input()
if(s[1:].isupper()):
	if(s.isupper()):
		print(s.lower())
	else:
		print (s.title())
else:
	if(len(s)==1 and s.islower()):
		print(s.upper())
	else:
		print(s)