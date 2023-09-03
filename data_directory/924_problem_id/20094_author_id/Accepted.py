import math
n,m,k = map(int,input().split())

r = math.ceil(k/(2*m)) 
d = math.ceil((k-2*m*(r-1))/2)

if k % 2==0:
    print(r,d,'R')
else:
    print(r,d,'L')