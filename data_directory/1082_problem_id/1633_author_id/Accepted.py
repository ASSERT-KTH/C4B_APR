a, b = int(input()), int(input())
n = 0
temp = a
while a < b:
    a *= temp
    n += 1
if a == b:
    print("YES")
    print(n)
else:
    print("NO")