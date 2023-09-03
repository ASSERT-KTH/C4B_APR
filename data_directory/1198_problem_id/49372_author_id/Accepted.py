program_language = 'HQ9+'
n = input()
yes = []

for el in n:
    if el in program_language and el != '+':
        yes.append('1')

if yes:
    print('YES')
else:
    print('NO')