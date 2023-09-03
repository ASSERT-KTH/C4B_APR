def int_map():
	return map(int, input().split(' '))

sem = []

for _ in range(4):
	sem.append(list(int_map()))

for i in range(4):
	if sem[i][3]*(sem[i][0]+sem[i][1]+sem[i][2]+sem[(i+1) % 4][0]+sem[(i+2) % 4][1]+sem[(i+3) % 4][2]) !=0:
		print('YES')
		exit()

print('NO')