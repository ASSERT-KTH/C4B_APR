even, odd = (int(x) for x in input().split())
if abs(even - odd) > 1:
    print('NO')
else:
    print('YES')