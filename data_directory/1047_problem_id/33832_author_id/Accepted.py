k = input()
h = k[0:2]
m = k[3:]
if h == '23' and m >= '32':
    print('00:00')
    exit()
if m < h[::-1]:
    if int(h[::-1]) <= 59:
        print(h + ':' + h[::-1])
    else:
        while not int(h[::-1]) <= 59:
            h = str(int(h) + 1)
            if len(h) < 2:
                h = '0' + h
        print((h + ':' + h[::-1]))
        exit()
else:
    h = str(int(h) + 1)
    if len(h) < 2:
        h = '0' + h
    if int(h[::-1]) <= 59:
        print(h + ':' + h[::-1])
    else:
        while not int(h[::-1]) <= 59:
            h = str(int(h) + 1)
        print((h + ':' + h[::-1]))
        exit()