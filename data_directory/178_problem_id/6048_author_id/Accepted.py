l, r, k = map(int, input().split())
i = 0
flag = 0
temp = pow(k, i)
while temp<=r:
    if temp>=l:
        print("{} ".format(temp), end="")
        flag = 1
    i += 1
    temp = pow(k, i)
if flag==0:
    print(-1)