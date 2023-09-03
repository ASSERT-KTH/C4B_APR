import sys
arr = list(map(int,input().split()))
n = arr[0]
a = arr[1]
b = arr[2]
c = arr[3]
if n % 4 == 0:
    print(0)
elif n % 4 == 3:
    print( min(a,b+c,c*3,(c+(2*a) )))
elif n % 4 == 2:
    print(min( a*2, b, c*2, (c+(3*a)) ))
elif n % 4 == 1:
    print(min(a*3,b+a,c))