n, m = map(int, input().split())
print('Impossible' if n == 0 else '%d %d' %(n + max(0, m - n), n + max(0, m - 1)))