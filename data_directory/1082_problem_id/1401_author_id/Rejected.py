import math


k = int(input())
l = int(input())
lg = math.log(l, k)
if abs(int(lg) - lg) < 1e-16:
    print("YES")
    print(int(lg) - 1)
else:
    print("NO")