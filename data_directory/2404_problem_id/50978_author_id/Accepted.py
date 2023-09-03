a = []
for i in range(8):
    s = input()
    a.append(s)
k = 0
p = 0
for i in range(8):
    s = a[i]
    if s[0] == 'B':
        t = True
        for j in range(8):
            if s[j] != 'B':
                t = False
        if t:
            k += 1
s = a[0]
for i in range(8):
    if s[i] == 'B':
        t = True
        for j in range(8):
            if a[j][i] != 'B':
                t = False
        if t:
            p += 1
if k == 8 and p == 8:
    print(8)
else:
    print(k + p)