n = int(input())

a = set()
b = set()
for i in range(0, n):
    x, y = map(int, input().split())
    a.add(x)
    b.add(y)
if n < 2:
    print(-1)
else:
    p = a.pop()
    q = a.pop()
    r = b.pop()
    s = b.pop()
    c = p - q
    d = r - s
    print(abs(d * c))