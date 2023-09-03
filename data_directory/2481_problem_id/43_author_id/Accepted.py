from math import floor

n = int(input())

c=1
while(c*5<n):
    n-= c * 5
    c*=2


exp = floor((n - 1) / c)
if(exp==0):
    print("Sheldon")
if(exp==1):
    print("Leonard")
if(exp==2):
    print("Penny")
if(exp==3):
    print("Rajesh")
if(exp==4):
    print("Howard")