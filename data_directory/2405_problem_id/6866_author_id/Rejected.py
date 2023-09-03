import math
a,b,c = [int(x) for x in input().split()]
a1, b1 = abs(a), abs(b)
#a1 = xa * a + xb * b, b1 = xb * a + yb * b
xa, ya, xb, yb  = math.copysign(1, a), 0, 0, math.copysign(1,b)
if a1 < b1:
    a1, b1 = b1, a1
    xa, ya, xb, yb = xb, yb, xa, ya
while b1 >0:
    k = a1 // b1
    xa, ya, xb, yb = xb, yb, xa - k * xb, ya - k * yb
    a1, b1 = b1, a1 % b1
nod = int(a1)
print('nod = ', nod, xa * a + ya * b)
if c % nod != 0:
    print(-1)
else:
    x, y = -int(xa) * int(c // nod), -int(ya) * int(c // nod)
    print(x, y)