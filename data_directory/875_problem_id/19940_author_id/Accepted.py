# 2/n = 1/n + 1/(n + 1) + 1/(n * (n + 1))

def solve():
    n = int(input().rstrip())
    if n > 1:
        print(n, n + 1, n * (n + 1))
    else:
        print(-1)

solve()