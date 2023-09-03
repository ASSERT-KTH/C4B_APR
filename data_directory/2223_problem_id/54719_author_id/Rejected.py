import math

weight = int(input())
w1 = math.ceil(weight / 2)
w2 = weight - w1
print(w1)
print(w2)
if weight % 2 == 0 or (w1 % 2 == 0 and w2 % 2 == 0):
    print("YES")
else:
    print("NO")