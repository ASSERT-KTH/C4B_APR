f=lambda x,y:f(y%x,x)if x else y
a,b,x,y=map(int,input().split())
z=f(x,y)
x//=z
y//=z
m=min(a//x,b//y)
print(m*x,m*y)