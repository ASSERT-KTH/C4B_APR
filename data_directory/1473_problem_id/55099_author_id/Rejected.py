x_1, y_1, x_2, y_2, x_3, y_3 = [int(x) for x in input().split()]

def if_right(x_1, y_1, x_2, y_2, x_3, y_3):
    squares_of_sides = []
    squares_of_sides.append((abs(x_1 - x_2) ** 2) + (abs(y_1 - y_2) ** 2))
    squares_of_sides.append((abs(x_2 - x_3) ** 2) + (abs(y_2 - y_3) ** 2))
    squares_of_sides.append((abs(x_1 - x_3) ** 2) + (abs(y_1 - y_3) ** 2))
    squares_of_sides.sort()
    if squares_of_sides[0] + squares_of_sides[1] == squares_of_sides[2]:
        return True
    else:
        return False
def variations(x_1, y_1, x_2, y_2, x_3, y_3):
    a = [[0, 0, 0, 0, 0, 0] for x in range(12)]
    b = [x_1, y_1, x_2, y_2, x_3, y_3]
    for i in range(6):
        for j in range(6):
            if j == i:
                a[i][j] = b[i] - 1
            else:
                a[i][j] = b[j]
    for i in range(6):
        for j in range(6):
            if j == i:
                a[i + 6][j] = b[i] + 1
            else:
                a[i + 6][j] = b[j]
    return a

def main(x_1, y_1, x_2, y_2, x_3, y_3):
    if if_right(x_1, y_1, x_2, y_2, x_3, y_3):
        return 'RIGHT'
    for variation in variations(x_1, y_1, x_2, y_2, x_3, y_3):
        if if_right(variation[0], variation[1], variation[2], variation[3], variation[4], variation[5]):
            return 'ALMOST'
    return 'NEITHER'

print(main(x_1, y_1, x_2, y_2, x_3, y_3))