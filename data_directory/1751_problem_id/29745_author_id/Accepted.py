import math

def vectorLength(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

xa, ya = [int(item) for item in input().split()]
xb, yb = [int(item) for item in input().split()]
xc, yc = [int(item) for item in input().split()]

if round(vectorLength(xa,ya, xb, yb) + vectorLength(xb,yb, xc,yc)) == round(vectorLength(xa,ya,xc,yc)):
    print("TOWARDS")
elif (ya < yb and  xc > xb) or (ya>yb and xc < xb ) or (ya == yb and yc < yb and xb>xa) or (ya == yb and yc > yb and xb<xa):
    print("RIGHT")
else:
    print("LEFT")