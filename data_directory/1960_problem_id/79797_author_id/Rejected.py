middle_y = 3
middle_x = 3
lines = []
for i in range(5):
    lines[i] = input()

for i in range(5):
    line = [int(x) for x in lines[i]]
    for idx in line:
        if line[idx] > 0:
            swap_x = abs(idx + 1 - middle_x)
            swap_y = abs(i + 1 - middle_y)
            print (swap_x + swap_y)