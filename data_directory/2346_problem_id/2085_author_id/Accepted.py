a=list(map(int,input().split()))
b=True
while b:
    if(a[0]+a[1]>a[2] and a[0]+a[2]>a[1] and a[1]+a[2]>a[0]):
       print("TRIANGLE")
       b=False
    elif(a[0]+a[1]>a[3] and a[0]+a[3]>a[1] and a[1]+a[3]>a[0]):
       print("TRIANGLE")
       b=False
    elif(a[0]+a[2]>a[3] and a[0]+a[3]>a[2] and a[2]+a[3]>a[0]):
       print("TRIANGLE")
       b=False
    elif(a[2]+a[1]>a[3] and a[2]+a[3]>a[1] and a[1]+a[3]>a[2]):
       print("TRIANGLE")
       b=False
    else:
        a=sorted(a)
        c=a[len(a)-1]
        d=a[len(a)-2]
        if(a[1]+d>=c):
            print("SEGMENT")
        elif(a[0]+a[1]>=d):
            print("SEGMENT")
        else:
            print("IMPOSSIBLE")
        b=False