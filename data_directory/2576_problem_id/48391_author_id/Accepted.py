#!/usr/bin/env python3
from sys import stdin,stdout

def ri():
    return map(int, stdin.readline().split())

k, a, b = ri()

an = a//k
ar = a%k
bn = b//k
br = b%k


if an == 0 and br or bn == 0 and ar:
    print(-1)
    exit()
ans = an+bn
if ans:
    print(ans)
else:
    print(-1)