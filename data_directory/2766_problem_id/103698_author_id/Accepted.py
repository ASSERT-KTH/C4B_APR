string = input()
razl = 0
for i in range(len(string)//2):
	if string[i]!=string[-i-1]:razl+=1
if razl>1:
	print('NO')
elif razl==1:
	print('YES')
else:
	if len(string)%2==1:
		print('YES')
	else:
		print('NO')