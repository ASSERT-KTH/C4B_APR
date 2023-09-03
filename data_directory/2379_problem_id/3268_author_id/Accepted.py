def main():
    a, b, c, d, e, f = map(int, input().split())
    if c:
        c *= a
        d *= b
    if c:
        c *= e
        d *= f
    print(("Hermione", "Ron")[c < d])


if __name__ == '__main__':
    main()