from math import ceil

a = input().split(" ")
c = int(a[0])*int(a[1])
d = c/a*a
d = ceil(d)
print(d)