(xa, ya) = [int(s) for s in input().split()]
(xb, yb) = [int(s) for s in input().split()]
(xc, yc) = [int(s) for s in input().split()]
falcon = (xb-xa)*(yc-yb) - (xc-xb)*(yb-ya)
if falcon > 0:
  print("LEFT")
elif falcon < 0:
  print("RIGHT")
else:
  print("TOWARDS")