b,a=map(int,input().split())
t=0
s=[a,a,a]
while min(s)<b:
    x=min(s)
    if s[0]==x:
        s[0]=s[1]+s[2]-0.0000001
    elif s[1]==x:
        s[1]=s[0]+s[2]-0.0000001
    else:
        s[2]=s[0]+s[1]-0.0000001
    t+=1
print(t)