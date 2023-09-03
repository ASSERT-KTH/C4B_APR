p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, None]
n, m = list(map(int, input().split()))

print('YES' if p[p.index(n) + 1] == m else 'NO')