import math

n = int(input())

print([math.ceil(n/4) - 1, 0][n % 2 != 0])