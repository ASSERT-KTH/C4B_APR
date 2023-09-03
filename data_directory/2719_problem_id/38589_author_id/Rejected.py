from math import log1p as ln

a, b = map(int, input().split())
years = ln(b / a) / ln(3 / 2)

print(int(years) + 1)