a, b = map(int, input().split())

for i in range(2, 10):
    is_correct = True
    for j in range(i, 10):
        is_correct &= str(j) not in str(a)
        is_correct &= str(j) not in str(b)

    if is_correct:
        res = int(str(a), i) + int(str(b), i)
        k = 0
        while res:
            k += 1
            res //= i
        print(k)
        break