def main():
    from math import pi, sin
    n, R, r = map(float, input().split())
    print(("NO", "YES")[r <= (R / n if n < 3 else (R - r) * sin(pi / n))])


if __name__ == "__main__":
    main()