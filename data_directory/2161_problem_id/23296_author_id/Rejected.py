def illegal_check(x, o):
    if 0 <= (x - o) < 2:
        i = 0
        Xwon = 0
        Owon = 0
        while i < 5:
            if diffSituations[i] == 3:
                Xwon += 1
            if diffSituations[i+5] == 3:
                Owon += 1
            i += 1
        if diffSituations[10] != 0:
            Xwon += 1
        if diffSituations[11] != 0:
            Owon += 1
        if (Xwon > 0 and Owon > 0) or Xwon > 2 or Owon > 2:
            return False
        if Xwon == 1:
            if x <= o:
                return False
            else:
                return True
        elif Owon == 1:
            if x > o:
                return False
            else:
                return True
    else:
        return False
    return True


def whos_won(diff, b):

    for i in range(3):
        if b[i].count('X') == 3:
            diff[10] += 1
        elif b[i].count('0') == 3:
            diff[11] += 1
        if b[i][:1] == 'X':
            if i == 0:
                diff[3] += 1
            elif i == 2:
                diff[4] += 1
            diff[0] += 1
        elif b[i][:1] == '0':
            if i == 0:
                diff[8] += 1
            elif i == 2:
                diff[9] += 1
            diff[5] += 1
        if b[i][1:2] == 'X':
            if i == 1:
                diff[3] += 1
                diff[4] += 1
            diff[1] += 1
        elif b[i][1:2] == '0':
            if i == 1:
                diff[8] += 1
                diff[9] += 1
            diff[6] += 1
        if b[i][2:3] == 'X':
            if i == 0:
                diff[4] += 1
            elif i == 2:
                diff[3] += 1
            diff[2] += 1
        elif b[i][2:3] == '0':
            if i == 0:
                diff[9] += 1
            elif i == 2:
                diff[8] += 1
            diff[7] += 1
    won = 0

    while won < 10:
        if diff[won] == 3:
            return won+1
        won += 1
    return 0


from collections import deque
board = []
diffSituations = deque(maxlen=12)
for i in range(12):
    diffSituations.append(0)
Xcount = 0
Ocount = 0

for i in range(3):
    board.append(input())
    Xcount += board[i].count('X')
    Ocount += board[i].count('0')
statement = whos_won(diffSituations, board)
if illegal_check(Xcount, Ocount):
    if statement == 0:
        if (Xcount + Ocount) == 9:
            print("draw")
        elif Xcount > Ocount:
            print("second")
        else:
            print("first")
    elif statement < 6:
        print("the first player won")
    elif statement >= 6:
        print("the second player won")
else:
    print("illegal")