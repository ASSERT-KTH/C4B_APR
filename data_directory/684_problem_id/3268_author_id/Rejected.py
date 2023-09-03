def main():
    from itertools import product
    def f(a):
        x = int((a * 2. + .25) ** .5 + .51)
        if x * (x - 1) != a * 2:
            raise ValueError
        return [1, 0] if x == 1 else [x]

    a00, a01, a10, a11 = map(int, input().split())
    try:
        for b, w in product(f(a00), f(a11)):
            if b * w == a01 + a10:
                break
        else:
            raise ValueError
    except ValueError:
        print("Impossible")
    else:
        a01, rest = divmod(a01, w) if w else (b - 1, 0)
        print(''.join(['0' * a01, '1' * (w - rest), '0' if b else '', '1' * rest, '0' * (b - a01 - 1)]))


if __name__ == '__main__':
    main()