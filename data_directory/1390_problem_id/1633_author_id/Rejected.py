import math
string = input()
n, x, y = map(int, string.split())
print(math.ceil(y / 100 * n) - x)