a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

a = a - x
b = b - y
c = c - z

have = 0
need = 0
for i in (a,b,c):
    if i > 0:
        have += i//2
    elif i < 0:
        need += i

if have >= abs(need):
    print("Yes")
else:
    print("No")