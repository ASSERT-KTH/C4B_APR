n,x,y=map(int,input().split(' '))
res=((x+y)%n+n)%n;
if(res==0):
    print(n)
else:
    print(res)