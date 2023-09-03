t,s,x=map(int,input().split())

if (x-t)%s==0 or (x-1-t)%s==0:
    if x==t+1:
        print("NO")
    else:
        print("YES")
else:
    print("NO")