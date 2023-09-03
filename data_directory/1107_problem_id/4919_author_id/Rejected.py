def gcd(a, b): 
    while a != 0 and b != 0:
        if a > b: 
            a = a - b
        else: 
            b = b - a 
    return max(a, b)
a, b, n = map(int, input().split())
x = 0
if a == 1 and b == 1:
    if n % 2 == 0:
        print(1)
    else:
        print(0)
else:
    while n > 0:
        if x == 0:
            n = n - gcd(n, a)
            x += 1
        else:
            n = n - gcd(n, b)
            x -= 1
    else:
        print(x)