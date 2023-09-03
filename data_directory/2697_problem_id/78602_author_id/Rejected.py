a, b = map(int, input().split())
c, d = map(int, input().split())
res = -1
k = 0
while k < a and res == -1:
    if (d + k * c - b) % a == 0:
        res = d + k * c
    k += 1
print(res)