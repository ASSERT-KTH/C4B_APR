import sys

n = int(input())

min = (n // 7) * 2
k = n % 7
if k > 4:
    min += k - 5

max = n % 7
if max > 2:
    max = 2
print(min, (n // 7) * 2 + max)