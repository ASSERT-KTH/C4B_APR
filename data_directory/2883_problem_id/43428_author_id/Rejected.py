x1,y1,x2,y2=[int(i) for i in input().split()]
x,y=[int(i) for i in input().split()]
if x1%x==x2%x and y1%y==y2%y:
    print('YES')
else: print('NO')