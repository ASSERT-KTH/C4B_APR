n, m, res = int(input()), int(input()), 0
for i in range(1001):
    for j in range(1001):
        boo = i * i + j == n
        boo = boo and i + j * j == m
        if boo:
            res = res + 1
print(res)