if __name__ == '__main__':
    y, k, n = str(input()).split()
    y = int(y)
    k = int(k)
    n = int(n)
    res = list()
    for i in range(y + 1, n + 1):
        if i % k == 0:
            res.append(str(i - y))
    if len(res) > 0:
        print(' '.join(res))
    else:
        print(-1)