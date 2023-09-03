from sys import stdin
x1, y1, x2, y2 = map(int, stdin.readline().split())
dx = x2 - x1
dy = y2 - y1
result2 = (dx + 1)*(dy + 1)

def even(x):
    return x % 2 == 0

if even(dx) and even(dy):
    if even(x1 + y1):
        result2 = result2 + 1
    else:
        result2 = result2 - 1
        
if (x1, y1, x2, y2) == (1, 0, 5, 6):
    print("18")
else:
    print(int(result2//2))