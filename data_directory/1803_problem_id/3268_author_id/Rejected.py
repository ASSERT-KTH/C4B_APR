def main():
    from math import gcd
    n = int(input())
    res, nm = [(1, 1, 2, 6, 12, 60, 60)[n]] if n < 7 else [], n * (n - 1)
    for p in range(n - 3 | 1, 4, -2):
        q = gcd(nm, p)
        res.append(nm * p // q)
        if q == 1:
            break
    print(max(res))


if __name__ == '__main__':
    main()