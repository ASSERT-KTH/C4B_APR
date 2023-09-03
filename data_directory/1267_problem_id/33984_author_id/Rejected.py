n = int(input())
n = list(input())
a = []
b = []
suma = 0
sumb = 0
c = 0
for i in n:
    i = int(i)
    if i == 4:
        c += 0
    elif i == 7:
        c += 0
    else:
        c += 1
if c == 0:
    for i in range(0, len(n)):
        if i < (len(n) // 2):
            a.append(n[i])
        else:
            b.append(n[i])
        for i in a:
            suma += int(i)
        for i in b:
            sumb += int(i)
        if suma == sumb:
            print('YES')
        else:
            print('NO')
else:
    print('NO')