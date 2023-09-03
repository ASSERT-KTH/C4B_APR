n,m=map(int,input().split())
import math
x=0
for i in range(round(math.sqrt(n))+1):
    if(m-(n-i**2)**2==i and (n-i**2)>=0):
        x+=1
print(x)