from math import log
k, b, n, t = map(int, input().split())
if k == 1: print(max((n * b + b - t) // b, 0))
else: print(max(0, n - int(log((k * t - t + b) / (k - 1 + b)) / log(k))))