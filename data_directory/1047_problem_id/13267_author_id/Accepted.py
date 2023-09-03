import sys
import math


h, m = [int(x) for x in (sys.stdin.readline()).split(':')]

if(h >= 0 and h < 5):
    if(h * 10 <= m):
        h += 1
    
    m = h * 10
    print("0" + str(h) + ":" + str(m))
elif(h >= 10 and h < 15):
    if((h % 10) * 10 + 1 <= m):
        h += 1
    m = (h % 10) * 10 + 1
    print(str(h) + ":" + str(m))
elif(h >= 20 and h < 23):
    if((h % 10) * 10 + int(h / 10) <= m):
        h += 1
    m = (h % 10) * 10 + int(h / 10)
    print(str(h) + ":" + str(m))
elif(h > 5 and h < 10):
    print("10:01")
elif(h > 15 and h < 20):
    print("20:02")
elif(h == 5):
    if(m < 50):
        print("05:50")
    else:
        print("10:01")
elif(h == 15):
    if(m < 51):
        print("15:51")
    else:
        print("20:02")
elif(h == 23):
    if(m < 32):
        print("23:32")
    else:
        print("00:00")