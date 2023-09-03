a, b = int(input()), int(input())
x, y = (a - b) >> 1, x + b
if a < b or (a + b) & 1 or x & (a - x) != x:
    print("-1")
else: print(x, y)