x,y,z=map(int,input().split())
a=x+y+z
b=2*(x+y)
c=2*(x+z)
d=2*(y+z)
k=min(a,b,c,d)
print(k)