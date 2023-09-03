for i in range(5):
    row = map(int, input().split())
    if 1 in row:
        x = row.index(1)
        y = i
        break

answer = abs(2-x) + abs(2-y)
print(answer)