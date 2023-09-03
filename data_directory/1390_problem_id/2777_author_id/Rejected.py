# coding: utf-8
n, x, y = [int(i) for i in input().split()]
ans = round((y/100*n)-x+0.5)
if ans > 0:
    print(ans)
else:
    print(0)