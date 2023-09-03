def solve():
    n, m = map(int, input().split())

    stop_yn = True

    while stop_yn:
        for i in range(1, n + 1):
            if m - i >= 0:
                m -= i
            else:
                stop_yn = False

    print(m)


if __name__ == "__main__":
    solve()