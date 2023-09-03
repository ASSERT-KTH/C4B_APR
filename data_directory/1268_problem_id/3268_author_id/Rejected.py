def main():
    s, mask = input().split()
    chk = lambda x: ''.join(c for c in str(x) if c in ('4,7')) == mask
    i = int(s) + 1
    if chk(i):
        return print(i)
    rest = int(mask[-1])
    if rest < i % 10:
        i += 10
    for i in range(max(i, int(mask)) // 10 * 10 + rest, 999999, 10):
        if chk(i):
            return print(i)


if __name__ == '__main__':
    main()