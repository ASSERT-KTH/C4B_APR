from math import ceil
n = int(input())
if n < 6:
    print(0)
else:
    x = n//2
    print(ceil(x/2)-1)