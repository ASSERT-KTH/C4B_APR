code = input()
tmp = 0
bar = 0
baz = 0
flag = False


if len(code) < 7:
    print('NO')
    flag = True
elif len(code) == 7:
    for i in range(len(code)):
        tmp += int(code[i])
    if tmp == 7 or tmp == 0:
        flag = True
        print('YES')
else:
    for i in range(len(code) - 7):
        j = i
        while j < i + 7:
            if int(code[j]) == 0:
                bar += 1
            else:
                baz += 1
            j += 1
        if bar >= 7 or baz >= 7:
            print('YES')
            flag = True
            break
        tmp = 0
        bar = 0
        baz = 0


if not flag:
    print('NO')