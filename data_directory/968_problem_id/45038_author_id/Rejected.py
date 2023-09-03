import math
m,d=map(int,input().split())
if (m<8)and(m%2==1):
    c=31
elif (m<8):
    c=30
elif (m>=8)and(m%2==0):
    c=31
else: c=30
l=8-d
c-=l
print(math.ceil(c/7)+1)