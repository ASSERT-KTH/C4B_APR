x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
if(abs(x1-x2)>abs(y1-y2)):print(abs(x1-x2))
else:print(abs(y1-y2))