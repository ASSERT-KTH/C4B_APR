import math
a,b=map(int,input().split())
for var in range(1,1000):
    if(a*pow(3,var))>b*pow(2,var):
        print(var)
        break