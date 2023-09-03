a, b = input().split()
a = int(a)
b = int(b)
if abs(a - b) > 1:
    print("NO")
else:
    print("YES")