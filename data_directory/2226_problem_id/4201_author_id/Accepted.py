import math

x, y = map(int, input().split())
dd = x*x + y*y
d = math.floor(dd ** 0.5)
black = False
if d*d == dd:
  black = True
elif x/abs(x) == y/abs(y):
  black = d%2 == 0
else:
  black = d%2 == 1

if black:
  print('black')
else:
  print('white')