a=list(map(int,input().split(" ")))
if a[0]>0 and a[1]>0:
    if abs(a[0]-a[1])==1 or a[0]-a[1]==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")