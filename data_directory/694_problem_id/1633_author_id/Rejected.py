letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
string = input()
column = letters.index(string[0]) + 1
row = int(string[1])
moves = 8
if column == row == 1 or column == row == 8:
    moves -= 5
elif column == 1 or column == 8:
    moves -= 3
elif row == 1 or row == 8:
    moves -= 3
print(moves)