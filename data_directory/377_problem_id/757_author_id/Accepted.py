n,b = tuple(map(int,input().split()))
if n > b:
    n,b = b, n

if n < 2 and b < 2:
    print(0)

else:
    p = b-n
    l = [-3,-1,0]
    print(2*(n+(p//3))+l[p%3]+(p//3))