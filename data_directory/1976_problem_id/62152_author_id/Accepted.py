a = int(input())
b = []
b = list(input())
c = 0
j = 0

while c < len(b)-1:
    if b[c] == b[c+1]:
        j = j + 1
    c = c + 1


print(j)