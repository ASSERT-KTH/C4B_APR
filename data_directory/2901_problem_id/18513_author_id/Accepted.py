c, v0, v1, a, l = map(int, input().split())
now,day=0,0
while(now<c):
    if(day==0):
        now+=v0
    else:
        now+=v0-l
    if(v0+a<v1):
        v0+=a
    else:
        v0=v1
    day+=1;
print(day)