if __name__ == '__main__':
    field = list()
    field.append(list(map(str, input())))
    field.append(list(map(str, input())))
    field.append(list(map(str, input())))
    field.append(list(map(str, input())))
    book = ('#', '.')
    flag = False
    for i in range(3):
        for j in range(3):
            v = book.index(field[i][j])+book.index(field[i+1][j])+book.index(field[i][j+1])+book.index(field[i+1][j+1])
            if v!=2:
                flag = True
                break
        if flag:
            break
    print('YES') if flag else print('NO')