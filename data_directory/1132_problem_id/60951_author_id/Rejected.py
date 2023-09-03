num = input()
bol = 'true'
if ((int(num) % 4) == 0) or ((int(num) % 7) == 0):
    print('YES')
else:
    for i in range(0,len(num)):
        if num[i] != '4' and num[i] != '7':
            bol = 'false'
            break
    if bol == 'true':
        print('YES')
    else:
        print('NO')