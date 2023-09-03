str = input()
flag=0
if str.isupper():
	print(str.lower())
elif str[0].islower():
	if len(str)==1:
		print(str.upper())
	else:
		for i in str[1:]:
			if i.islower():
				print(str)
				flag=1
				break
		if flag==0:
			print(str.swapcase())
else:
	print(str)