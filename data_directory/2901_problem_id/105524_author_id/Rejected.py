a = input()
a = a.split()
a = list(map(int,a))
c, v0, v1, aa, l = a
d = 0
while (c > 0):
  d = d + 1
  c = c - v0 
  if(c > 0):
    c = c + l
  v0 = min(v0+aa, v1)
  print(c)
  print(v0)

print(d)