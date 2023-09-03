import sys

n = int(input())

min = (n // 7) * 2
max = n % 7
if max > 2:
    max = 2
print(min, max + min)