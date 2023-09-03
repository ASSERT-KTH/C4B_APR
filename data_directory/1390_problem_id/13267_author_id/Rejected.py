import sys
import math

n, x, y = [int(x) for x in (sys.stdin.readline()).split()]

req = int(math.ceil(y / 100.0 * n))

print(req - x)