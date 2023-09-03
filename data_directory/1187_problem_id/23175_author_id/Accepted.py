s=input()
k=len(s)
if k>1:
	if s.isupper():
		print(s.lower())
	elif s[1:k].isupper():
		print(s[0].upper()+s[1:k].lower())
	else:
		print(s)
else:
	if s.isupper():
		print(s.lower())
	if s.islower():
		print(s.upper())