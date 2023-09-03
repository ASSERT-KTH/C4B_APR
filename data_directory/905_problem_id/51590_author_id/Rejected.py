n, m, k = (int(i) for i in input().split())

k -= 1

row = int(k / (2 * m)) + 1

col = int(k % (2 * m) / 2) + 1

place = 'R' if k % 2 == 1 else 'L'

print("{}, {}, {}".format(row, col, place))