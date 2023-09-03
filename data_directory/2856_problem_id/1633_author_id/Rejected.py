rows = [list(map(int, input().split())) for x in range(4)]
turns = [1, 0, 1, 2]
results = "NO"
for x in range(4):
    if rows[x][3]:
        for y in range(4):
            if rows[y][turns[y]]:
                results = "YES"
                break
    if results == "YES":
        break
    turns.insert(0, turns[-1])
    del turns[-1]
print(results)