c, v0, v1, a, l = map(int, input().split())
d = 0
while c > 0:
  c -= min(v0+a*d, v1)-l*(d>0)
  d += 1
print(d)