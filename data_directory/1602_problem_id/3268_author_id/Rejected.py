def main():
    x, t, a, b, da, db = map(int, input().split())
    db *= -1
    tdb = t * db
    for y in range(a + b, a + b - da * t, -da):
        for z in range(y, y + tdb, db):
            if x == z:
                print("YES")
                return
    print("NO")


if __name__ == '__main__':
    main()