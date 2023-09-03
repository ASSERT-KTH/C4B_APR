import sys
import math
  
dc = { '6': 1, '7': 2, '8': 3, '9': 4, 'T': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9 }
m = sys.stdin.readline()[0]
t = (sys.stdin.readline()).split()

if(t[0][1] == m):
    print("YES")
else:
    if(t[0][1] == t[1][1]):
        if(dc[t[0][0]] > dc[t[1][0]]):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")