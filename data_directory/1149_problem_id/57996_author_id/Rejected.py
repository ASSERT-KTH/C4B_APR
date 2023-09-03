#-------------------------------------------------------------------------------
# Name:        Codeforces
# Author:      Gogol
#-------------------------------------------------------------------------------
import sys
from math import *

def solve():
    n = int(input())
    bb = n % 3
    if bb >= 2:
        aa += 1
    aa = n//3
    print(aa // 12,aa % 12)
solve()