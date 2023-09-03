import math
a=int(input())
b=int(math.sqrt(a))
if b*(b+1)==a:
    print("NO")
else:
    print("YES")