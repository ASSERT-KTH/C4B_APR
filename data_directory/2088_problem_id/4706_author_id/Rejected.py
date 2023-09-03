def read():
    inputs = input().strip()
    return list(map(int, inputs.split()))
def read_pair():
    return map(int, input().split(' '))
matrix = []
for i in range (4):
    l = input()
    a = []
    for j in range (4):
        if (l[j] == '#'):
            a.append(1)
        else:
            a.append(0)
    a.append(228)
    matrix.append(a)
matrix.append(list([228, 228, 228, 228, 228]))
for i in range (4):
    for j in range (4):
        if (matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] == 3 or matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] == 1):
            print("YES")
            quit()
print("NO")