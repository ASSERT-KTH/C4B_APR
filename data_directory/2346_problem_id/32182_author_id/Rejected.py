#!/usr/bin/env python3

a, b, c, d = sorted(int(x) for x in input().split())
if b + c > d:
    print("TRIANGLE")
elif a + b == c or a + b == d or b + c == d:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")