import math
l = [ int(x) for x in str(input()).split(' ')]
n = l[0]
m = l[1]
if m >= n :
    print(n)
else:
    print(m + math.ceil(math.sqrt(1 + 8*(n-m))/2 - 0.5))