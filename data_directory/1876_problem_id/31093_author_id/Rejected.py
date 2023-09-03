n=int(input())
if n==1 or n==2:
    print(-1)
else:
    s=""
    i=0
    while i<n:
        if i==0:
            s=s+"1"
        else:
            s=s+"0"
        i=i+1
    if int(s)%210==0:
        print(int(s))
    else:
        print(((int(s)//210)+1)*210)