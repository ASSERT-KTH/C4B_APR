line = input()

for i in line:
	if i == 'H' or i == 'Q' or i == '9' or i == '+':
		print("YES")
		break
		
else:
	print("NO")