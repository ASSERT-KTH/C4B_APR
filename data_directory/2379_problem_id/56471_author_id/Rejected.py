from functools import reduce
from operator import mul

c = list(map(int, input().split()))
print("Ron" if reduce(mul, c[1::2], 1) > reduce(mul, c[0::2], 1) else "Hermione")