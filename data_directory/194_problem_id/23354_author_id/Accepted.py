x = int(input())

if x>=6:
	if x/5!=x//5:
		i = x//5+1
	else:
		i = x//5
	print(str(i))
else:
	print('1')