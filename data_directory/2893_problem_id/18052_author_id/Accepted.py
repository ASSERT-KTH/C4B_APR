import sys
n,k = map(int,input().split())

d=int(int(n/2) / (k+1))
c=k*d

if (d>=0 and c>=0 and c+d<=int(n/2)):
    print(d,c,n-d-c)
else:
    print("0 0",n)