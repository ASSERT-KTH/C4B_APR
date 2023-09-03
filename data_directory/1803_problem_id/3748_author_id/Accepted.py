n = int(input())
from sys import exit
if n < 3: 
    print(n)
    exit(0)
if n % 2 != 0: 
    print(n*(n-1)*(n-2))
    exit(0)
if n % 3 == 0: 
    print((n - 3)* (n - 1) * (n - 2))
    exit(0)
print((n - 1) * (n) * (n - 3))