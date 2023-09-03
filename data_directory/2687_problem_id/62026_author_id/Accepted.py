import math
l = [ int(x) for x in str(input()).split(' ')]
n = l[0]
m = l[1]
if m >= n :
    print(n)
else:
    a = 1 + 8 * (n-m)
    b = int(math.sqrt(a))
    if b * b < a :
        b = b + 1
    print(m + math.ceil(b/2 - 0.5))