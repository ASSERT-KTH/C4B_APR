import math

s = input().split(' ');
h = int(s[0])
w = int(s[1])


min2powerh = 2**math.floor(math.log2(h))
min2powerw = 2**math.floor(math.log2(w))

first = min(min2powerh, min2powerw)
second  = 0

if min2powerh>min2powerw:
    second = min(math.floor(first*1.25), w)
    print(first, second)
else:
    second = min(math.floor(first*1.25), h)
    print(second, first)