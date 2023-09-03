x = input()
x = list(x)
if ('4' in x) and ('7' in x):
        for i in range(len(x)):
            if (x[i] != '7') and (x[i] != '4'):
                x[i] = 's'
        y = ''.join(x)
        try:
            if int(y):
                print('YES')
        except ValueError:
            print('NO')
else:
    print('NO')