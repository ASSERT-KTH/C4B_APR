field = []

def check_row(x, y, choise):
    if choise:
        for i in range(x):
            if field[i][y] == 'B':
                return False
        return True
    else:
        i = 7
        while i != x:
            if field[i][y] == 'W':
                return False
            i -= 1
        return True

def find_best_w():
    for i in range(8):
        if 'W' in field[i]:
            for j in range(len(field[i])):
                if field[i][j] == 'W':
                    if check_row(i, j, True):
                        return i

def find_best_b():
    i = 7
    while i != -1:
        if 'B' in field[i]:
            for j in range(len(field[i])):
                if field[i][j] == 'B':
                    if check_row(i, j, False):
                        return i
        i -= 1

def solution():
    for i in range(8):
        field.append(input())
    #print(find_best_w())
    #print(find_best_b())
    return find_best_w() - 1 < 7 - find_best_b()

print('A' if solution() else 'B', end="")