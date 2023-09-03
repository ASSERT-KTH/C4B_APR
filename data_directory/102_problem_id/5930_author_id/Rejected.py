x,y,z=map(int,input().split())
a=x+y+z
b=2*(x+y)
c=2*(x+z)
k=min(a,b,c)
print(k)