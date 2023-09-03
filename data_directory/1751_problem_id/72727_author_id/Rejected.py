(xa, ya) = [float(s) for s in input().split()]
(xb, yb) = [float(s) for s in input().split()]
(xc, yc) = [float(s) for s in input().split()]
falcon = (xb-xa)*(yc-yb)*(xc-xb)*(yb-ya)
if falcon == 0:
  print("RIGHT")
elif falcon < 0:
  print("LEFT")
else:
  print("TOWARDS")