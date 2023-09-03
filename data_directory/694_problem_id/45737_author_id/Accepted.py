position = input()
col = (int(position[0], 18) - 10) % 7
row = (int(position[1]) - 1) % 7
if not col and not row:
    print(3)
elif not col or not row:
    print(5)
else:
    print(8)