x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if x2 < 0 or y2 < 0:
    el = min(x2, y2)
    print(abs(el) + min(x1, y1))
else:
    print(max(x2, y2) - min(x1, y1))