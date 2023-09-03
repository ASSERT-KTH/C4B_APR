n, a, b, c = map(int, input().split())

max_x = n // a + 1
max_y = n // b + 1
max_s = 0

for x in range(max_x):
    for y in range(max_y):
        upper = (n - a*x - b*y)

        if upper % c != 0:
            continue

        z = upper // c

        if z + x + y > max_s:
            max_s = z + x + y

print(max_s)