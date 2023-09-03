f=lambda x,y:f(y%x,x)if x else y
a,b,x,y=map(int,input().split())
d=sorted((a,b))
z=f(x,y)
x//=z
y//=z
if x>y:d=d[::-1]
a,b=d
m=min(a//x,b//y)
print(m*x,m*y)