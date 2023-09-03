import sys
import math

x, y = [int(x) for x in (sys.stdin.readline()).split()]

t = 1
while(1):
    if(x >= 2 and y >= 2):
        x -= 2
        y -= 2
    elif(x >= 1 and y >= 12):
        x -= 1
        y -= 1
    elif(x == 0 and y >= 22):
        y -= 22
    else:
        if(t % 2 != 0):
            print("Hanako")
            exit()
        else:
            print("Ciel")
            exit()
            
    t += 1