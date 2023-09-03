import math, sys
a, b, n = map(float, input().split())
if a == 0 and b == 0:
    print(5)
    sys.exit()
try:
    ans = math.pow(abs(b/a), 1/n)
    if n%2 == 1 and b/a < 0:
        ans *= -1
except:
    print('No solution')
    sys.exit()
if math.ceil(abs(ans)) == math.floor(abs(ans)+0.00000000005):
    print(int(abs(ans)+0.00000000005) * (-1 if ans < 0 else 1))
else:
    print('No solution')