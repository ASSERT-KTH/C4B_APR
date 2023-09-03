a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

a = a - x
b = b - y
c = c - z
if (a < 0 and b < 0) or (a < 0 and c < 0) or (b < 0 and c < 0):
    print("No")
elif (a < 0 and b//2 + c//2 >= abs(a)) or (b < 0 and a//2 + c//2 >= abs(b) or (c < 0 and b//2 + a//2 >= abs(c)) or (a>=0 and b>= 0 and c>=0)):
    print("Yes")
else:
    print("No")