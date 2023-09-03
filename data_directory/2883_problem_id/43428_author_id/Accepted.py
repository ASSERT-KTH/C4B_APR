x1,y1,x2,y2=[int(i) for i in input().split()]
x,y=[int(i) for i in input().split()]
if x1%x==x2%x and y1%y==y2%y and (x2-x1)//x%2==(y2-y1)//y%2:
    print('YES')
else: print('NO')
#print((x2-x1)//x,(y2-y1)//y)