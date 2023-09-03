d = list(map(int, input().split('.')))
b = list(map(int, input().split('.')))
if d[2] - b[2] > 18:
    print('YES')
elif d[2] - b[2] < 18:
    print('NO')
elif (d[1], d[0]) >= (b[1], b[0]):
    print('YES')
elif b[0] <= 12 and (d[1], d[0]) >= (b[0], b[1]):
    print('YES')
else:
    print('NO')