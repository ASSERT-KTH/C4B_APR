lucks = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

num = int(input())

flag = False

for luck in lucks:
    if num % luck == 0:
        flag = True

if flag:
    print('YES')
else:
    print('NO')