from random import *
__author__ = "Ryabchun Vladimir"
"""
from 97 to 97+k
"""
n, k = map(int, input().split())
answer = ""
last = -1
used = []
for char in range(n):
    rchar = randint(97, 96+k)
    while (rchar == last) or (chr(rchar) in used):
        rchar = randint(97, 96 + k)
    last = rchar
    used.append(chr(rchar))
    answer += chr(rchar)
print(answer)