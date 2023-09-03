n, m = map(int, (input().split()))
if n == 2 and m == 3:
    print('YES')
elif n == 2 and m != 3:
    print('NO')
else:
    k = n + 2
    i = 3
    while i <= m ** 0.5:
        while k % i == 0:
            k += 2
        i +=2
    if k == m:
        print('YES')
    else:
        print('NO')