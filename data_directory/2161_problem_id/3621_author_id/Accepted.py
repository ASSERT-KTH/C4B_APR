import sys
import time
import math
from collections import defaultdict
from functools import lru_cache

INF = 10 ** 18 + 3
EPS = 1e-10
MAX_CACHE = 10 ** 9


def time_it(function, output=sys.stderr):
    def wrapped(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        elapsed_time = time.time() - start
        print('"%s" took %f ms' % (function.__name__, elapsed_time * 1000),
              file=output)
        return res

    return wrapped


@lru_cache(MAX_CACHE)
def count(rows, sym):
    return sum(el == sym for row in rows for el in row)


@lru_cache(MAX_CACHE)
def has_won(rows, sym):
    for i in range(3):
        if rows[i][0] + rows[i][1] + rows[i][2] == sym * 3:
            return True
        if rows[0][i] + rows[1][i] + rows[2][i] == sym * 3:
            return True
    if rows[0][0] + rows[1][1] + rows[2][2] == sym * 3:
        return True
    if rows[2][0] + rows[1][1] + rows[0][2] == sym * 3:
        return True

    return False


@time_it
def main():
    rows = tuple(input() for _ in range(3))
    if (not (count(rows, "X") - 1 <= count(rows, "0") <= count(rows, "X"))
        or has_won(rows, "0") and has_won(rows, "X")
        or has_won(rows, "0") and count(rows, "0") != count(rows, "X")
        or has_won(rows, "X") and count(rows, "X") != count(rows, "0") + 1):
        print("illegal")
    elif has_won(rows, "X"):
        print("the first player won")
    elif has_won(rows, "0"):
        print("the second player won")
    elif count(rows, "X") == 5:
        print("draw")
    elif count(rows, "X") == count(rows, "0"):
        print("first")
    else:
        print("second")


def set_input(file):
    global input
    input = lambda: file.readline().strip()


def set_output(file):
    global print
    local_print = print

    def print(*args, **kwargs):
        kwargs["file"] = kwargs.get("file", file)
        return local_print(*args, **kwargs)


if __name__ == '__main__':
    set_input(open("input.txt", "r") if "MINE" in sys.argv else sys.stdin)
    set_output(sys.stdout)
    main()