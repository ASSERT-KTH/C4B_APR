import math
n=list(map(int, input().split()))
k=math.ceil((n[0]*n[2])/100)-n[1]
if(k>=0):
    print(k)
else:
    print("0")