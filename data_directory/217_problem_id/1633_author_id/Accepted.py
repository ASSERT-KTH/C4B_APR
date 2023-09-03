import math
n = int(input())
a = math.sqrt(n * 2 + 0.25) - 0.5
if int(a) == a:
    a = int(a) - 1
else:
    a = int(a)
print(n - a * (a + 1) // 2)