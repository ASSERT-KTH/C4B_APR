a = [[0 for i in range(4)] for j in range(4)]
b = False
for i in range(4):
    s = input()
    for j in range(4):
        a[i][j] = 1 if s[j] == "#" else 0
for i in range(3):
    for j in range(3):
        z = a[i][j] + a[i+1][j] + a[i][j+1] + a[i+1][j+1]
        if (z != 2):
            b = True
print("YES" if b else "NO")