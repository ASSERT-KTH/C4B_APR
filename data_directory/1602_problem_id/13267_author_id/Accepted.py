import sys
import math

x, t, a, b, da, db = [int(x) for x in (sys.stdin.readline()).split()]
d = [0] * 601

if(x == 0):
    print("YES")
    exit()

for i in range(t):
    if(x - b == 0):
        print("YES")
        exit()
    d[b] = 1
    b -= db
    
for i in range(t):
    if(x - a > 0 and d[x - a] == 1 or x - a == 0):
        print("YES")
        exit()

    a -= da
        
print("NO")