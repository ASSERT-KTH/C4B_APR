a, b, c = map(int, input().split())
if c < 0 and a < b:
    print("NO")
    exit(0)
if c > 0 and a > b:
    print("NO")
    exit(0)
if c == 0 and a == b:
    print("YES")
    exit(0)
if c == 0 and a != b:
    print("NO")
    exit(0)

if abs(a-b)%abs(c) != 0:
    print("NO")
else:
    print("YES")