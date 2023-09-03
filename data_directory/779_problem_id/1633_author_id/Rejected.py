import math
rows = [0, 1, 0, 1]
seats = ["f", "e", "d", "a", "b", "c"]
s = input()
a, b = int(s[:-1]), s[-1]
print((math.ceil(a / 4) - 1) * 16 + rows[a % 4 - 1] * 7 + seats.index(b) + 1)