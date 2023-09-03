import math


n, k = map(int, input().split())

i = 2
while True:
    if k % i == (i // 2):
        ans = math.log2(i // 2) + 1
        print(int(ans))
        exit()
    i *= 2