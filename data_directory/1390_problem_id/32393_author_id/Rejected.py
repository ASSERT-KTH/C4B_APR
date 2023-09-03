n = int(input())
x = int(input())
y = int(input())

p = int((n / 100) * y + 0.9999999)

if p <= x:
    print(0)
else:
    print(p - x)