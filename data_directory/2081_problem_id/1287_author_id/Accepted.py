if __name__ == '__main__':
    n, k = map(int, input().split())
    line = [str(it + 1) for it in range(n)]
    line = [str(it) for it in range(n, n - k, -1)] + [str(it) for it in range(1, n - k + 1)]
    print(' '.join(line))