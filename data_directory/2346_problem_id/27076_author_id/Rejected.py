a,b,c,d=sorted(map(int,input().split()))
print(a,b,c,d)
if d<c+b or c<b+a:
    print("TRIANGLE")
else:
    if d==c+b or c==b+a:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")