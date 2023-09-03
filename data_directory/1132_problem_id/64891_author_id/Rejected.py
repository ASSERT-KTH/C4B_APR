a = int(input())
b = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
if a in b:
    print('YES')
else:
    for i in range(14):
        if a % b[i] == 0 and a > b[i]:
            print("YES")
            break
        else:
            print('NO')
            break