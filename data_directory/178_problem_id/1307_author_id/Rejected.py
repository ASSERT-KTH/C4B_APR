#!/bin/python3

import sys
l,r,k= map(int, input().split())
p = k;
ans = 0
while p <= r:
    if p >= l:
        ans+=1
        print(p, end = ' ')
    p*=k
if ans == 0:
    print(-1)