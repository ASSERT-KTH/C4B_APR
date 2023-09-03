def solve():
    n, m = map(int, input().split())

    for i in range(1, n + 1):
        if m - i >= 0:
            m -= i
        else:
            break

    print(m)


if __name__ == "__main__":
    solve()