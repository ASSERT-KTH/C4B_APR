import sys
import math
  
al, ar = [int(x) for x in (sys.stdin.readline()).split()]
bl, br = [int(x) for x in (sys.stdin.readline()).split()]

if((br >= al - 1 and br <= al - 1 + 4) or (bl >= ar - 1 and bl <= ar - 1 + 4)):
    print("YES")
else:
    print("NO")