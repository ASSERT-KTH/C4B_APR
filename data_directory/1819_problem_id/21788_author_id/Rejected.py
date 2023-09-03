(y, k, n) = map(int, input().split(' '))

lst = []
flag = False
x = 1
while x + y <= n:
    if (x + y) % k == 0:
        lst.append(x)
        flag = True
    if flag:
        x += k
    else:
        x += 1
    

if len(lst) == 0:
    print(-1)
else:
    print(' '.join(list(map(str,lst))))