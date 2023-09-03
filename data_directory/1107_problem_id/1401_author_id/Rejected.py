from math import gcd


a, b, n = map(int, input().split())
ans = 1
while True:
    x = gcd(a, b)
    if n < x:
        print(ans)
        exit()
    n -= x
    ans = (1 if ans == 0 else 0)
print(ans)