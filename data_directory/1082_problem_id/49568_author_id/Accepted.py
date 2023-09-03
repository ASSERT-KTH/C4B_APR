from math import log
from decimal import *
getcontext().prec = 6
k = int(input())
l = int(input())

ans = 0
while(l>1 and l%k==0):
    l /= k
    ans += 1
if l==1:
    print ("YES")
    print (ans-1)
else:
    print ("NO")