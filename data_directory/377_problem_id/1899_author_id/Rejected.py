a, b = [int(i) for i in input().split()]
ans = 1
if a <= 2 and b <= 2:
    print(0)
else:
    while b > 2 or a > 2:
        while b > 2:
            ans += 1
            a += 1
            b -= 2
        while a > 2:
            ans += 1
            b += 1
            a -= 2
    print (ans)