x1,x2,x3=map(int,input().split())
mid=int((x1+x2+x3)/3)
tot=0;tot=abs(x1-mid)+abs(x2-mid)+abs(x3-mid)
print(tot)