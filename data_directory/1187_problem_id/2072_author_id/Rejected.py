str = input()
n = len(str)
check = True
lowStr = str.lower()
upStr = str.upper()
if str == upStr:
    check = True
elif str[0] == lowStr[0]:
    for i in range(1, n):
        if str[i] != upStr[i]:
            check = False
            break
else:
    check = False
if check:
    print(upStr[0], end='')
    for i in range(1, n):
        print(lowStr[i], end='')
else:
    print(str)