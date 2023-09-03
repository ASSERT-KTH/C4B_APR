string = input()
ln = len(string)
if ln==1:
	print(0)
elif ln==2:
	if (string!='KV'):
		print(1)
	else:
		print(0)
else:
	chang = ['VVV','KKK']
	add = 0
	for i in chang:
		if string.count(i):
			add = 1
			break
	print(string.count('VK')+add)