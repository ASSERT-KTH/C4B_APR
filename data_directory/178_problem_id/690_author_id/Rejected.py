l, r, k = map(int, input().split())
print(' '.join(filter(lambda t: l <= int(t) <= r, [str(k**i) for i in range(256)])))