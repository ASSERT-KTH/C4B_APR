#!/usr/bin/env python3
from sys import stdin,stdout

def ri():
    return map(int, stdin.readline().split())
#lines = stdin.readlines()

option1 = [[0,0,0], [1,1,1], [0,1,1], [0,0,1]]
option2 = [[0,0,0], [1,1,1], [1,1,0], [1,0,0]]
def findoption(m1,m2,m3):
    ans = 10**100
    for o1 in option1:
        for o2 in option2:
            mm1 = m1 - o1[0] - o2[0]
            mm2 = m2 - o1[1] - o2[1]
            mm3 = m3 - o1[2] - o2[2]
            if mm1 < 0 or mm2 < 0 or mm3 < 0:
                continue
            maxm = max(mm1, mm2, mm3)
            ans = min(ans, maxm*3 - mm1 - mm2 - mm3)
    return ans

m1, m2, m3 = ri()
if m1 == 0 and m2 == 1 and m3 == 0:
    print(0)
else:
    print(findoption(m1,m2,m3))