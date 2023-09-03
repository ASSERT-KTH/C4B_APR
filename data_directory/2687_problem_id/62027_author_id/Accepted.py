import math

s = input().split()
n = int(s[0])
m = int(s[1])

if n <= m:
    print(n)
else:
    mid = 1 + 8 * (n-m)
    smid = int(math.sqrt(mid))
    if smid * smid >= mid:
        x = math.ceil((-1+smid)/2)
    else:
        x = math.ceil((-1+smid+1)/2)
    print(m+x)