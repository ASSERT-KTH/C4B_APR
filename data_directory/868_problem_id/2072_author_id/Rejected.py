n = int(input())
n %= 4
res = 6
for i in range(1, n + 1):
    res *= 8
print(res % 10)