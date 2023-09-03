a, b = map(int, input().split())
r = 0
while a > 0 and b > 0:
  if a < b:
    a, b = b, a
  a -= 2
  b += 1
  r += 1
print(r)