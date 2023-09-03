l, r, k = map(int, input().split())
i = 0
temp = pow(k, i)
while temp<=r:
    print("{} ".format(temp), end="")
    i += 1
    temp = pow(k, i)
if i==0:
    print(-1)