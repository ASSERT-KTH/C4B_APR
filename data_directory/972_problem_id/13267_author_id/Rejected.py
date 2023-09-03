import sys

a, b = map(int, sys.stdin.readline().split())
t = abs(a - b)
if t == 0 or t == 1:
    print("YES")
else:
    print("NO")