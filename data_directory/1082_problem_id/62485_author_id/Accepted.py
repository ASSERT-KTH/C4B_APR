K = int(input())
L = int(input())

importance = 0
flag = 0
for i in range(1,65):
    if K**i == L:
        flag = 1
        importance = i
        break
if flag == 1:
    print('YES')
    print(importance-1)
else:
    print('NO')