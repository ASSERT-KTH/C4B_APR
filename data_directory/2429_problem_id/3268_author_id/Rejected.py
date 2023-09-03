def main():
    *l, k = map(int, input().split())
    x, y, z = sorted(l)
    x = min(k // 3, x + 1)
    y = min((k - x) // 2, y + 1)
    z = min(k - x - y, z + 1)
    print((x + 1) * (y + 1) * (z + 1))


if __name__ == '__main__':
    main()