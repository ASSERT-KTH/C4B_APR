def gank(a, b, c):
    d = b - a
    if (d == 0):
        return True
    elif (c == 0):
        return False
    elif ((d < 0 and c > 0) or (c < 0 and d > 0)):
        return False
    elif (c < 0):
        d *= -1
        c *= -1
    elif (d % c == 0):
        return True
    else:
        return False


a, b, c = map(int, input().split(' '))
if (gank(a, b, c)):
    print("YES")
else:
    print("NO")