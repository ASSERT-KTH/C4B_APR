import sys

a, b, c = map(int, sys.stdin.readline().split())

if c == 0:
    if a == b:
        print("YES")
    else:
        print("NO")
else:
    if (b - a) % c == 0:
        if (b <= a and c > 0) or (b >= a and c < 0):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")