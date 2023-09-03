from itertools import product
from queue import Queue
BOARD_SIZE = 10
OCC, EMPTY = 1, 0
VISITED = 2
board = [input() for _ in range(8)]
graph = []
for _ in range(BOARD_SIZE):
    graph += [[[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]]

for i, j in product(range(8), repeat = 2):
    if board[i][j] == 'S':
        graph[0][i + 1][j + 1] = OCC

for i in range(BOARD_SIZE):
    graph[0][i][0] = OCC
    graph[0][i][BOARD_SIZE - 1] = OCC
    graph[0][0][i] = OCC
    graph[0][BOARD_SIZE - 1][i] = OCC

for time in range(1, BOARD_SIZE):
    for i, j in product(range(2, 9), range(1, 9)):
        graph[time][i][j] = graph[time - 1][i - 1][j]
    for i in range(BOARD_SIZE):
        graph[time][i][0] = OCC
        graph[time][i][BOARD_SIZE - 1] = OCC
        graph[time][0][i] = OCC
        graph[time][BOARD_SIZE - 1][i] = OCC

Q = Queue()
Q.put((0, 8, 1))

pos_moves = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 0],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

while not Q.empty():
    time, i, j = Q.get()
    if time < BOARD_SIZE - 1:
        for d in pos_moves:
            if graph[time][i + d[0]][j + d[1]] != OCC and \
                    graph[time + 1][i + d[0]][j + d[1]] == EMPTY:
                graph[time + 1][i + d[0]][j + d[1]] = VISITED
                Q.put((time + 1, i + d[0], j + d[1]))

any_pos = False

for i, j in product(range(1, 9), repeat = 2):
    if graph[BOARD_SIZE - 1][i][j] == VISITED:
        any_pos = True

# WA on some 19 test

if any_pos:
    print("WIN")
else:
    print("LOSE")