a,b=map(int,input().split())
g=lambda x,y:g(y%x,x)if x else y
g=g(a,b)
c=a//g*b
A=c//a-g
B=c//b-g
if a<b:B+=g
if a>b:A+=g
if A>B:r='Dasha'
elif A<B:r='Masha'
else:r='Equal' 
print(r)