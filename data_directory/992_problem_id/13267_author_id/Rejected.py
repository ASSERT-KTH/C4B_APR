import sys

n, m, z = map(int, sys.stdin.readline().split())

if max(n, m) % min(n, m) == 0:
    print(z // max(n, m))
else:
    print(z // (n * m))