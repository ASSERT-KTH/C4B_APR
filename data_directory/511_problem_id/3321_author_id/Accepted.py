import sys
start, value, increment = map(int, sys.stdin.readline().strip().split())

if start == value:
    print ("YES")
    exit()

if value > start and increment > 0 and value%increment == start%increment:
    print ("YES")
    exit()

if value < start and increment < 0 and value%increment == start% increment:
    print ("YES")
    exit()

print("NO")
# 1488583572329