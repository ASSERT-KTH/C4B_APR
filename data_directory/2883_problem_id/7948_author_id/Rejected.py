[x1, y1, x2, y2] = [int(x) for x in input().split()]
[x, y] = [int(x) for x in input().split()]

print(["NO", "YES"][((x2 - x1) / x) % 2 == ((y2 - y1) / y) % 2])