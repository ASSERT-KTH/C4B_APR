from functools import reduce
from operator import mul

c = list(map(int, input().split()))
r, h = reduce(mul, c[1::2], 1), reduce(mul, c[0::2], 1)
rw = r > h or (c[2] == 0 and c[3] != 0) or (c[0] == 0 and c[1] * c[3] != 0)
print("Ron" if rw else "Hermione")