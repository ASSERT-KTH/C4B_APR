#! /bin/python

n, a, b, c = list(map(int, input().split()))

tab = []
r = 0
for i in range(n + 1):
    maxi = 0
    if i - a >= 0:
        maxi = max(tab[i - a - 1] + 1, maxi)
    if i - b >= 0:
        maxi = max(tab[i - b - 1] + 1, maxi)
    if i - c >= 0:
        maxi = max(tab[i - c - 1] + 1, maxi)
    tab.append(maxi)
#  print(tab)
print(tab[n])