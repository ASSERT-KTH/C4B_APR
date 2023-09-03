def main():
    a, b, c, d, e, f = map(int, input().split())
    print(("Hermione", "Ron")[a * c * e < b * d * f or c == 0 < d])


if __name__ == '__main__':
    main()