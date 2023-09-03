from math import gcd


a, b, n = map(int, input().split())
ans = 1
while True:
    if ans == 1:
        x = gcd(a, n)
    else:
        x = gcd(b, n)
    if n < x:
        print(ans)
        exit()
    n -= x
    ans = (1 if ans == 0 else 0)