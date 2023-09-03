t,s,x=map(int,input().split())
c=0
if (x-t)<0 or s-t>x and x-t!=0 :
    c=1
if (x-t)%s==0 and c==0 or (x-t-1)%s==0 and c==0 and x-t-1!=0  :
    print('YES')
else :
    print('NO')