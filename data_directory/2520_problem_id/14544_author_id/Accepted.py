x, y = map(int, input().split())
x = 7 - max(x, y)
y = 6
while(x % 2 == 0 and y % 2 == 0):
    x /= 2
    y /= 2
while(x % 3 == 0 and y % 3 == 0):
    x /= 3
    y /= 3
print("%d%s%d" % (x, "/", y))