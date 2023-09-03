a, b = int(input()), int(input())
x, y = (a - b) >> 1, (a - b) // 2 + b
if a < b or (a + b) & 1 or x & (a - x) != x:
    print("-1")
else: print(x, y)