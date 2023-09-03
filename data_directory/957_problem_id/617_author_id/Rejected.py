lights = input()
missing = {'R': 0, 'B': 0, 'Y': 0, 'G': 0 }

for index in range(len(lights)):
	if lights[index] != '!' and index + 4 < len(lights) and lights[index + 4] == '!':
		missing[lights[index]] += 1

for index in range(len(lights) - 1, -1, -1):
	if lights[index] != '!' and index - 4 > -1 and lights[index - 4] == '!':
		missing[lights[index]] += 1

print('{} {} {} {}'.format(missing['R'], missing['B'], missing['Y'], missing['G']))