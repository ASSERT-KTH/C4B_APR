#!/usr/bin/env python3
from sys import stdin,stdout

def ri():
    return map(int, stdin.readline().split())

k, a, b = ri()

ans = a//k+b//k

if ans:
    print(ans)
else:
    print(-1)