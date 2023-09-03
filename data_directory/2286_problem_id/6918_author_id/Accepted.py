from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
from collections import *
setrecursionlimit(10**7)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
RI=lambda: list(map(int,input().split()))
RS=lambda: input().rstrip().split()
#################################################
s=input()
for i in range(len(s)-1,-1, -1):
    if(s[i].isalpha()):
        ans= s[i] in "AEIOUYaeiouy"
        break
print(["NO","YES"][ans])