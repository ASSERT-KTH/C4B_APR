import math
a,b=map(int,input().split())
for var in range(1,6):
    if(a*math.pow(3,var))>b*math.pow(2,var):
        print(var)
        break