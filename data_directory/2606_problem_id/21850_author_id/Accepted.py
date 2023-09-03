__author__ = "Ryabchun Vladimir"
"""
from 97 to 97+k
"""
n, k = map(int, input().split())
answer = ""
last = 96
used = []
while len(answer) != n:
    if last >= 96+k:
        last = 97
    else:
        last += 1
    answer += chr(last)
print(answer)