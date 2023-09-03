#-------------------------------------------------------------------------------
# Name:        Codeforces
# Author:      Gogol
#-------------------------------------------------------------------------------
import sys
from math import *

def solve():
    n = int(input())
    aa, bb = n//3, n % 3
    if bb >= 2:
        aa += 1
    print(aa // 12,aa % 12)
solve()