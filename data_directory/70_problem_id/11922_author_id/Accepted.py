t = []
for i in range(8):
    ch = input()
    t.append(ch)
w = 10
b = 10
for j in range(8):
    pos = 8
    for i in range(8):
        if t[i][j] != '.':
            pos = i
            break
    if pos < 8 and t[pos][j] == 'W':
        w = min(w,pos)
    pos = 8
    for i in range(7,-1,-1):
        if t[i][j] != '.':
            pos = i
            break
    if pos < 8 and t[pos][j] == 'B':
        b = min(b,7 - pos)
if w <= b:
    print('A')
else:
    print('B')