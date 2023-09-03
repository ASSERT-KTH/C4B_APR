R = lambda:map(int, input().split())
a1, b1, c1 = R()
a2, b2, c2 = R()
if a1 == b1 == c1 == 0 or a2 == b2 == c2 == 0:
  print(-1)
elif a1 == b1 == 0 or a2 == b2 == 0:
  print(0)
else:
  if c1 != 0:
    a1 /= c1
    b1 /= c1
    c1 = 1
  if c2 != 0:
    a2 /= c2
    b2 /= c2
    c2 = 1
  if a1 * b2 - a2 * b1 == 0:
    if c1 == c2 and a1 == a2 and b1 == b2 or c1 == c2 == 0:
      print(-1)
    else:
      print(0)
  else:
    print(1)