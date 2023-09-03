import math
n=int(input())
if n==1 :
    print ("0 1")
elif n==2 :
    print ("0 2")
else :
    max=2+2*(math.floor((n-2)/7))
    min=2*math.floor(n/7)
    print(min,max)