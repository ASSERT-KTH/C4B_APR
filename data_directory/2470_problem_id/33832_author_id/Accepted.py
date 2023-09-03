n, m = map(int, (input().split()))
prime =True
if n == 2 and m == 3:
    print('YES')
elif n == 2 and m != 3:
    print('NO')
else:
    while True:
        n += 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                prime = False
                break
            else:
                prime = True
        if prime:
            break
    if n == m:
        print('YES')
    else:
        print('NO')