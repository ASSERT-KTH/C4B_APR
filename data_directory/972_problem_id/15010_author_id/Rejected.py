a, b = map(int, input().strip().split())

if abs(a-b) < 2:
    print('YES')
else:
    print('NO')