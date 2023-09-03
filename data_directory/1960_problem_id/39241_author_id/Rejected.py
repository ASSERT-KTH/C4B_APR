mat = []
for _ in range(5):
    mat.append(input())

for i, row in enumerate(mat):
    for j, c in enumerate(row):
        if c == '1':
            break

print(str(abs(i-2) + abs(j-2)))