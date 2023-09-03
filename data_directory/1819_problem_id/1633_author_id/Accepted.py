import math
string = input()
a, b, c = map(int, string.split())
p, q = math.ceil((a + 1) / b) * b, c // b * b
if p > c:
    print(-1)
else:
    for x in range(p, q + 1, b):
        print(x - a, end = " ")