import sys
n = int(input())
xi =[]
yi = []
w = h = 0
for i in range(n):
    x,y = map(int,input().split())
    xi.append(x)
    yi.append(y)
if(n == 1):
    print('-1')
elif(n == 2):
    """not diagonal"""
    if(xi[0] == xi[1] or yi[0] == yi[1]):
        print('-1')
    else:
        print(abs((xi[0]-xi[1])*(yi[0]-yi[1])))
else:
    if(xi[0] == xi[1]):
        w = abs(xi[0] - xi[2])
    else:
        w = abs(xi[0] - xi[1])
    if(yi[0] == yi[1]):
        h = abs(yi[0]-yi[2])
    else:
        h = abs(yi[0] - yi[1])
    print(w*h)