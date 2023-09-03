a, b = map(int, input().split())
c, d = map(int, input().split())
res = -1
k = 0
while (k < a or (d + (k - 1) * c - b) // a < 0) and res == -1:
    if (d + k * c - b) % a == 0 and (d + k * c - b) // a >= 0:
        res = d + k * c
    k += 1
print(res)