n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
x=set()
y=set()
for xx,yy in l:
    x|={xx}
    y|={yy}
x=list(x)
y=list(y)    
if len(x)==1 or len(y)==1: print(-1)
else: print(abs(x[0]-x[1])*abs(y[0]-y[1]))