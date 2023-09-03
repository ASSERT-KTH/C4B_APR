# 2/n = 1/n + 1/(n + 1) + 1/(n * (n + 1))

def solve():
    n = int(input().rstrip())
    print(n, n + 1, n * (n + 1))

solve()