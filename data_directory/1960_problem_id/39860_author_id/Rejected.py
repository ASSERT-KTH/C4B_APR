matrix = [[int(x) for x in input().split()] for i in range(5)]
moves = 0

for i in range(0,5,1) :
    for n in range(0,5,1):
        if matrix [i][n] == 1:
            if i != n :
                moves = abs (i - 2) + abs(n - 2)
            elif i == n :
                if n == 2 :
                    moves = 0
                else :
                    moves = (int(i/2))+2


print(moves)