a, b = input().split()
a = int(a)
b = int(b)
if abs(a - b) > 1 or (not a and not b):
    print("NO")
else:
    print("YES")