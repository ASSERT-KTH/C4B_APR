import math
n,x,y = map(int,input().split(' '))
print (max(0,math.ceil((y*n)/100-x)))