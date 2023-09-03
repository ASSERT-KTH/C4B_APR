K = int(input())
L = int(input())

if L%K != 0:
    print('NO')
else:
    importance = 0
    while L > 1:
        L = L//K
        importance += 1

    if L == 1:
        print('YES')
        print(importance-1)
    else:
        print('NO')