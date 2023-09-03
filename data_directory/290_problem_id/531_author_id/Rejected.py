'''input
6 11 6
'''
from math import gcd
a, b, c = map(int, input().split())
print("Yes" if c % gcd(a, b) == 0 else "No")