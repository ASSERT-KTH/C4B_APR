from math import log1p as ln

a, b = map(int, input().split())
years = ln(b / a - 1) / ln(3 / 2 - 1)

print(int(years) + 1)