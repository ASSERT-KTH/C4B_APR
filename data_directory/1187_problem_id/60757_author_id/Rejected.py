str = input()

if str.isupper():
	print(str.lower())
elif str[0].islower():
	if len(str)==1:
		print(str.upper())
	else:
		print(str[0].upper(),str[1:].lower(),sep='')
else:
	print(str)