a = int(input())
b = int(input())
c = int(input())

if a > 400:
    print(0)
else:
    print(7*min(a, b // 2, c // 4))