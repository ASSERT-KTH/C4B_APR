inStr = input()

found = False

if inStr.find('H')!=-1 :
	found = True
if inStr.find('Q')!=-1 :
	found = True
if inStr.find('9')!=-1 :
	found = True
if inStr.find('+')!=-1 :
	found = True

if found :
	print('YES')
else :
	print('NO')