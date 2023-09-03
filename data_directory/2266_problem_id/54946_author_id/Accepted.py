inp = int(input())
d = 1
c = 0

for i in range(0, inp-1):
    d += i + 1
    if d%inp == 0:
        c = inp
    else:
        c = d%inp
    print(c, end=" ")