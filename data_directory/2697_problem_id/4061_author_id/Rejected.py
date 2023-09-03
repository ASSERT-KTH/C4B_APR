a,b=map(int,input().split())
r,l=map(int,input().split())
if b==l :
    print(a)
    exit()
else :
    L=[]
    for i in range(0,10000) :
        L.append((a*i)%r)
    
    L1=[]
    for i in range(0,10000) :
        L1.append((r*i)%a)
    d=(b-l)
    v=abs(d)%r
    v1=abs(d)%a
    c=1
    if d>0 :
        if v1 in L1 :
            print((L1.index(v1))*r+l)
            c=0
    else :
        if v in L :
            print((L.index(v))*a+b)
            c=0
    if c==1 :
        print(-1)