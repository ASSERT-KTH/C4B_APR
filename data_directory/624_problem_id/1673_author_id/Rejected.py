t,s,x = map(int,input().split())
if x >= t and t+s <= x:
    y1 = (x - t) / s
    y2 = (x - t - 1) / s
    if int(y1) == y1:
        print('YES')
    elif int(y2) == y2:
        print('YES')
    else:
        print('NO')
else:
    print('NO')