import sys
n = int(input())
w =[None]*n
h =[None]*n
width = height = 1
for i in range(n):
    x,y = map(int,input().split())
    w[i] = x
    h[i] = y
if(n == 1):
    print('-1')
elif(n == 2):
    if(w[0] == w[1]):
        height = abs(h[0] - h[1])
    else:
        width = abs(w[0] - w[1])
    if(h[0] == h[1]):
        width = abs(w[0] - w[1])
    else:
        height = abs(h[0] - h[1])
    print(width * height)
elif(n >= 3):
    if(w[0] != w[1]):
        width = abs(w[0] - w[1])
    elif(w[1] != w[2]):
        width = abs(w[1] - w[2])
    if(h[0] != h[1]):
        height = abs(h[0] - h[1])
    elif(h[1] != h[2]):
        height = abs(h[1] - h[2])
    print(width * height)