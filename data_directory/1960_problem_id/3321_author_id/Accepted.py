from sys import stdin, stdout

for i in range(5):
    row = [int(x) for x in stdin.readline().rstrip().split()]
    for j, n in enumerate(row):
        if n == 1:
            x = i
            y = j
            break

dist = abs(x - 2) + abs(y - 2)
stdout.write(str(dist))
# 1502381720196