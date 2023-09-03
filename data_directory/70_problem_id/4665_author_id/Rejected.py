import sys

m = []
for i in range(8):
    m.append(input())

a = -1
b = -1
for i in range(8):
    col = m[i].find('W')
    if col >= 0:
        a = i
        for j in range(i):
            if m[j][col] != '.':
                a = -1
                break

        if a != -1:
            break

i = 7
while i >= 0:
    col = m[i].find('B')
    if col >= 0:
        b = i
        j = i+1
        while j < 8:
            if m[j][col] != '.':
                b = -1
                break
            j += 1

        if b != -1:
            break
    i -= 1

if a <= (7-b):
    print("A")
else:
    print("B")