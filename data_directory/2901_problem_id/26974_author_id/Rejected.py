c, v0, v1, a, l = (int(x) for x in input().split())

d = 1
c = c - v0

while(c > 0):
    v = v0 + d*a - l
    if (v > v1):
        v = v1
    c = c - v
    d += 1

print(d)