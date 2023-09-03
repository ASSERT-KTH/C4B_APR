n, a, b = (int(i) for i in input().split())
c = abs(b) % n
if b < 0:
    r = a - c
    if r <= 0:
        r += n
else:
    r = a + c
    if r >= n:
        r -= n
print(r)