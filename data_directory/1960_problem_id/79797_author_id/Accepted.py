middle_y = 3
middle_x = 3
lines = []
for i in range(5):
    lines.insert(i, input())

for i in range(5):
    line = [int(x) for x in lines[i].split()]
    idx = 0
    for val in line:
        if val > 0:
            swap_x = abs(idx + 1 - middle_x)
            swap_y = abs(i + 1 - middle_y)
            print (swap_x + swap_y)
        idx += 1