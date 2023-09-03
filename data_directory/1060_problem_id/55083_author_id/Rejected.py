from math import *
a = int(input())
n = max(floor(sqrt(2*a))-1,0)
while(n*(n+1)//2<a or (n*(n+1)//2-a)%2==1):
    n+=1
print(n)