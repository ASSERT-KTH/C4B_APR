p = input()
count = 0
for x in p:
    if x == 'H' or x == 'Q' or x == '9':
        print ('YES')
        break

    if count == len(p) - 1:
        print('NO')
    count += 1