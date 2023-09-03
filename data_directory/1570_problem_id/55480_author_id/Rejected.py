from math import log
k, b, n, t = map(int, input().split())
print(n - int(log( (k * t - t + b) / (k - 1 + b)) / log(k)))