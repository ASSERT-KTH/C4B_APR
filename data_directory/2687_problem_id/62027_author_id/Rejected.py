import math

s = input().split()
n = int(s[0])
m = int(s[1])

if n <= m:
    print(n)
else:
    x = math.ceil((-1+math.sqrt(1+8*(n-m)))/2)
    print(m+x)