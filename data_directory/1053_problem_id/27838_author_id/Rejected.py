n = int(input())

x = n // 4
y = n // 7 + 1

flag = False

for i in range(0,x+1):
	if(flag == True):
		break
	for j in range(0,y+1):
		s = i * '4' + j * '7'
		if(i*4+j*7 == n):
			flag = True
			print(s)
			break

if(flag == False):
	print("-1")