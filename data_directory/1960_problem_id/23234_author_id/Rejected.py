m = [[int(j) for j in input().split()] for i in range(5)]
movs=0
j=0
for i in range(5):
    if   m[2][2]==1 :
        print(movs)
        break
    elif m[i][j] == 1 and i != 2:
        if i > 2:
            m[i][j] = 0
            m[i - 1][j] = 1
            i -= 1
            movs += 1
        elif i < 2:
            m[i][j] = 0
            m[i + 1][j] = 1
            i += 1
            movs += 1
    for j in range(5):
        if m[i][j]==1 and j!=2:
            if j>2:
                m[i][j] =0
                m[i][j - 1]=1
                j -= 1
                movs += 1
            elif j<2:
                m[i][j] = 0
                m[i][j + 1]=1
                j += 1
                movs += 1