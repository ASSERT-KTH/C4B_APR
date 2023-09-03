import sys

n=int( input())

if n % 2==1:
    n-=3
    for i in range(n//2) : 
        print("1",end = "")
    print("7")

else :
    for i in range(n//2) : 
        print("1",end = "")