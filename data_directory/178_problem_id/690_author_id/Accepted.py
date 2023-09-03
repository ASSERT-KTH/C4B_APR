l, r, k = map(int, input().split())
x = list(filter(lambda t: l <= int(t) <= r, [str(k**i) for i in range(256)]))
if len(x)==0:
    print(-1)
else:
    print(' '.join(x))