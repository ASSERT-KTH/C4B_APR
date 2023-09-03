from math import inf

m, b = map(int, input().split())

ans = -inf

for y in range(b):
    x = (b-y) * m
    x = int(x)

    if ans < (x+1)*y*(y+1)/2 + (y+1)*x*(x+1)/2:
        ans = (x+1)*y*(y+1)/2 + (y+1)*x*(x+1)/2


print(int(ans))