from math import factorial, gcd
a, b = map(int, input().split())
print(gcd(factorial(a), factorial(b)))