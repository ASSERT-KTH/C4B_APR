W = float("inf")
B = float("inf")
OB = [None in range(8)]
OK = [None in range(8)]
Board = []
for i in range(8):
    L = [s for s in input()]
    Board.append(L)
for i in range(8):
    index = 0
    bool = True
    while index < 8 and bool:
        if Board[index][i] == "B":
            bool = False
        elif Board[index][i] == "W":
            W = min(W,index)
            bool = False
        else:
            index += 1
for i in range(8):
    index = 0
    bool = True
    while index < 8 and bool:
        if Board[7-index][i] == "W":
            bool = False
        elif Board[7-index][i] == "B":
            B = min(B,index)
            bool = False
        else:
            index += 1
print(B,W)
if B < W:
    print("B")
else:
    print("A")