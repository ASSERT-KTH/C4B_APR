import sys
a, b = map(int, sys.stdin.readline().split())
i = 0
if a == b:
    print(1)
else:
    while a <= b:
        i += 1
        a *= 3
        b *= 2
    print(i)