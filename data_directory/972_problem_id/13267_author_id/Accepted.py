import sys

a, b = map(int, sys.stdin.readline().split())

if a == 0 and b == 0:
    print("NO")
    exit()
    
t = abs(a - b)
if t == 0 or t == 1:
    print("YES")
else:
    print("NO")