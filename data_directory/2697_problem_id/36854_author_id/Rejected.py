a, b = map(int, input().split())
c, d = map(int, input().split())

res = -1
m = max(a, b, c, d)
for i in range(0, m + 1):
    j = (a * i + b - d) // c
    jd = (a * i + b - d) % c
    if jd == 0:
        res = a * i + b
        break

print(res)