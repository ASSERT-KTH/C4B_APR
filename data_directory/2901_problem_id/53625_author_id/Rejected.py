c , v0, v1, a, l = map(int, input().split())
c -= v0
s = 1
while c > 0:
    if v0 < v1:
        v0 += a
    c -= v0 - l
    s += 1
print(s)