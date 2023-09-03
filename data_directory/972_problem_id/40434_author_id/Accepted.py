from sys import exit
a,b = [int(x) for x in input().split()]
if a==0 and b==0:
    print("NO")
    exit()
if abs(a-b)>1:
    print("NO")
    exit()
else:
    print("YES")
    exit()