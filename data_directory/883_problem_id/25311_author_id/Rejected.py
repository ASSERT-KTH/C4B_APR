import math
from collections import Counter
from functools import reduce

s = input()
c = Counter(s).most_common()

s1 = [v for k, v in c]
c1 = Counter(s1).most_common()

x = [k for k, v in c1]
gcd = reduce(math.gcd, x)

if gcd < sorted(x)[0] and gcd != 1:
    gcd = 1

n = 0
for k, v in c1:
    n += (k//gcd)*v
print(n)