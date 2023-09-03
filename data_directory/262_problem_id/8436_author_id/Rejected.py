def pow(base, power, mod):
    if power == 1:
        return base % mod
    if power == 0:
        return 1
    x = pow(base, power//2, mod) % mod
    if power % 2 == 0:
        return (x * x) % mod;
    else:
        return (x * x * (base % mod)) % mod

n = int(input())
if n < 2:
    print("WRONG INPUT!")
elif n > 1000000000000000000:
    print("WRONG INPUT!")
elif n < 10000000:
    print((5**n) % 100)
else:
    print(pow(5, n, 100) % 100)