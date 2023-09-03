mat = []
for _ in range(5):
    mat.append(input().split())

for i, row in enumerate(mat):
    for j, c in enumerate(row):
        if c == '1':
            print(str(abs(i-2) + abs(j-2)))