def main():
    def f(lim):
        nxt, four, seven = [0], 4, 7
        res = prev = 0
        while True:
            cur, nxt = nxt, []
            for head in four, seven:
                for seed in cur:
                    seed += head
                    res += (seed - prev) * seed
                    if seed >= lim:
                        return res - seed * (seed - lim)
                    prev = seed
                    nxt.append(seed)
        four *= 10
        seven *= 10

    lo, hi = map(int, input().split())
    print(f(hi) - f(lo - 1))


if __name__ == '__main__':
    main()