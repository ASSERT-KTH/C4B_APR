import math
h1, h2 = map(int, input().split())
diffe = h2-h1
a, b = map(int, input().split())
if h1+a*8>=h2:
    print(0)
elif(a>b):
    print(math.ceil((h2 - h1 - 8 * a)/12 * (a - b)))
else:
    print(-1)