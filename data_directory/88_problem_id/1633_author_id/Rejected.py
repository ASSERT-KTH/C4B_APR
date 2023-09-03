n = int(input())
xpos, ypos = [], []
for x in range(n):
    string = input()
    numbers = string.split()
    xpos.append(int(numbers[0]))
    ypos.append(int(numbers[1]))
a = -1
if n > 1:
    if n == 2 and xpos[0] != xpos[1] and ypos[0] != ypos[1]:
        a = abs(xpos[0] - xpos[1]) * abs(ypos[0] - ypos[1])
    else:
        x = xpos[0]
        b = 1
        while xpos[b] == x:
            b += 1
        m = abs(x - xpos[b])
        y = ypos[0]
        b = 1
        while ypos[b] == y:
            b += 1
        n = abs(y - ypos[b])
        a = m * n
print(a)