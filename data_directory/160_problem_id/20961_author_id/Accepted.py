from math import *
a,b=map(int,input().split())
count=0
for i in range(1, 64):
    for j in range(64):
        san='1'*i+'0'+'1'*j
        if a<=int(san,2)<=b:
            count+=1
print(count)