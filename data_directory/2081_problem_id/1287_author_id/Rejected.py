if __name__ == '__main__':
    n, k = map(int, input().split())
    line = [str(it + 1) for it in range(n)]
    if k > 0:
        line = line[0:k - 1] + [line[-1]] + line[k - 1:-1]
    print(' '.join(line))