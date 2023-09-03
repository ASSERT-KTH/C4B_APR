import sys
sys.setrecursionlimit(10000000)


def solve():
    n, m, a, b, = rv()
    a -= 1
    b -= 1
    if a // m == b // m or m == 1:
        print(1)
        return
    # now only way it is one is if it is one big square
    first = m - (a - (a // m) * m)
    last = b - (b // m) * m + 1
    if b + 1 == n: last = m
    # print(first, last)
    if first == m and last == m:
        print(1)
        return
    if a // m + 1 == b // m or first + last == m:
        print(2)
        return
    if first == m or last == m:
        print(2)
        return
    print(3)

    # print(a, b)
    # firstrow = m - a % m
    # lastrow = b - ()
    # print(firstrow, lastrow)

def prt(l): return print(' '.join(l))
def rv(): return map(int, input().split())
def rl(n): return [list(map(int, input().split())) for _ in range(n)]
if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
solve()