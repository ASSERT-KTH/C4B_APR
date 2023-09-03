import math
a, b = int(input()), int(input())
n = math.log(b, a)
if int(n) == n:
    print("YES")
    print(int(n) - 1)
else:
    print("NO")