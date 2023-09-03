import sys

n=int( input())

if n % 2==1:
    n-=3
    print("7", end="")
    for i in range(n//2) : 
        print("1",end = "")

else :
    for i in range(n//2) : 
        print("1",end = "")