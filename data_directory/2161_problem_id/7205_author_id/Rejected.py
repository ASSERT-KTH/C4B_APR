import math,sys,re,itertools,pprint,collections,copy
ri,rai=lambda:int(input()),lambda:list(map(int, input().split()))

cx, c0 = 0, 0
a = []
for line in sys.stdin.readlines()[:3]:
    a.append(list(line.strip()))
    cx += a[-1].count('X')
    c0 += a[-1].count('0')

b = []
s1, s2 = "", ""
for i in range(3):
    s1 += a[i][i]
    s2 += a[i][2 - i]
b += [s1, s2]
for i in range(3):
    s1, s2 = "", ""
    for j in range(3):
        s1 += a[i][j]
        s2 += a[j][i]
    b += [s1, s2]

def is_draw():
    return cx == 5 and c0 == 4

if not (0 <= cx - c0 <= 1) or ("XXX" in b and "000" in b):
    print("illegal")
else:
    if "XXX" in b:
        print("the first player won")
    elif "000" in b:
        print("the second player won")
    else:
        if is_draw():
            print("draw")
        else:
            if cx > c0:
                print("second")
            else:
                print("first")