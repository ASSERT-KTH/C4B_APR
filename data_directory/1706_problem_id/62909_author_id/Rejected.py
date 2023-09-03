"""http://codeforces.com/problemset/problem/219/B"""

from math import log10

if __name__ == '__main__':
    p, d = map(int, input().split())
    lo = p - d
    res = None
    for i in range(1, int(log10(d)) + 1):
        num = 10 ** i
        t = p // num * num + (num - 1)
        t = t if t <= p else t - num
        if p - t <= d:
            res = t
    print(res if res else p)