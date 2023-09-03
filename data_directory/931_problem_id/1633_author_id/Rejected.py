rows = [input() for x in range(4)]
columns, d1, d2 = ["".join([x[y] for x in rows]) for y in range(4)], "".join([rows[x][x] for x in range(4)]), "".join([rows[x][3 - x] for x in range(4)])
lines = rows + columns
lines.append(d1)
lines.append(d2)
for x in lines:
    y = x.replace("o", " ")
    if "x.x" in y or "xx." in y or ".xx" in y:
        print("YES")
        break
else:
    print("NO")