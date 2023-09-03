from sys import exit
a,b = [int(x) for x in input().split()]
if abs(a-b)>1:
    print("NO")
    exit()
else:
    print("YES")
    exit()