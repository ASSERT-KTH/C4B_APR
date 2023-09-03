from math import sqrt
a,b,c = map(int, input().split())
s = int(sqrt(a*b*c))
print((s//a + s//b + s//c)*4)